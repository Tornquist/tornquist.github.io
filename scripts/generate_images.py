#!/usr/bin/env python
import os
import re
import shutil
from enum import Enum

from ImageMagick import ImageMagick

### Config

# Operational
START_KEY = '!@ generate_image '
END_KEY = '!@ end_generate'
TEMP_DIR = 'temp'
SEARCH_FOLDERS = ['_posts', '_projects']

# CSS
STYLESHEET = 'assets/styles/main.css'
PAGE_WIDTH_REGEX = '^.*--page-width: ([0-9]+)px;$'
IMAGE_GAP_REGEX = '^.*\.photo \+ \.photo { margin-left: ([0-9]+)px; }$'
DEFAULT_IMAGE_GAP = 6

### Operational Helpers

def ensure_dir_exists(dir):
  try:
    os.stat(dir)
  except:
    os.mkdir(dir)

def list_files(dir):
  return [dir + '/' + s for s in os.listdir(dir)]

def list_all_files(folders):
  files = [list_files(dir) for dir in folders]
  files = [item for sublist in files for item in sublist]
  return files

def progress_bar_if_configured(text, count):
  try:
    import progressbar

    widgets = [
      '{}: '.format(text),
      progressbar.Percentage(),
      ' ', progressbar.Bar(),
      ' ', progressbar.ETA(),
    ]

    bar = progressbar.ProgressBar(widgets=widgets,
                                  max_value=count,
                                  redirect_stdout=True).start()
  except ImportError:
    bar = None

  return bar

### Parsing Helpers

def identify_requests(lines):
  engaged = False

  outputFile = None
  inputFiles = []

  completeRequests = {}

  for line in lines:
    if line.startswith(START_KEY):
      outputFile = line.replace(START_KEY, '').strip()
      engaged = True if len(outputFile) > 3 else False
    elif line.startswith(END_KEY):
      if len(inputFiles) > 1:
        completeRequests[outputFile] = inputFiles
      engaged = False
      outputFile = None
      inputFiles = []
    elif engaged:
      inputFiles.append(line.strip())

  return completeRequests

def identify_all_requests(files):
  requests = {}
  for file in list_all_files(SEARCH_FOLDERS):
    with open(file, 'r') as fh:
      all_lines = fh.readlines()
      file_requests = identify_requests(all_lines)
      if len(file_requests) > 0:
        print(' ', file, ':', len(file_requests))
        requests = {**requests, **file_requests}
  return requests

### CSS Identification

def find_style_in_file(file, style_regex):
  with open(file) as fh:
    all_lines = fh.readlines()
    check = re.compile(style_regex)

    for line in all_lines:
      check_match = check.match(line)
      if check_match is not None:
        return int(check_match.group(1))

  return None

### Image Generation

def calculate_padding(num_images, true_image_width, page_size, image_gap):
  gaps = num_images - 1
  total_gap = image_gap * gaps
  displayed_image_size = (page_size - total_gap)/num_images
  padding = round(int(true_image_width) / displayed_image_size * image_gap)
  return padding

def generate(output, images, page_size, image_gap, bar = None):
  num_images = len(images)

  class Result(Enum):
    REPLACED  = 'Replaced '
    GENERATED = 'Generated'
    SKIPPED   = 'Skipped  '
    NO_CHANGE = 'No change'

  def log(result, message = ''):
    print('  [ {} ] {} {}'.format(result.value, output, message))

  # Ensure images are the same size.
  # This allows images to be directly chained (no zooming, scaling, etc)
  same_size, (width, height) = ImageMagick.check_same_size(images)
  if not same_size:
    log(Result.SKIPPED, 'Inconsistent image size')
    if bar is not None: bar += 1
    return

  # Identify if an image has been generated previously (enable compare logic)
  destination_exists = os.path.exists(request)
  destination = request if not destination_exists else temp_image_path

  # Calculate padding in pixel space of images (for consistent scaled display)
  padding = calculate_padding(len(images), width, page_size, image_gap)

  ImageMagick.generate(images, padding, destination)

  if destination_exists:
    try:
      ImageMagick.compare(temp_image_path, request)
      log(Result.NO_CHANGE)
    except Exception as e:
      log(Result.REPLACED)
      shutil.copyfile(temp_image_path, request)
  else:
    log(Result.GENERATED)

  if bar is not None: bar += 1

### Main Process

if __name__ == "__main__":
  # Identify all requests
  print("Scanning for image requests")

  files = list_all_files(SEARCH_FOLDERS)
  requests = identify_all_requests(files)

  if len(requests) == 0:
    print('No requests found')
    quit()

  # Identify destination
  page_size = find_style_in_file(STYLESHEET, PAGE_WIDTH_REGEX)
  image_gap = find_style_in_file(STYLESHEET, IMAGE_GAP_REGEX)

  if page_size is None:
    print('Error: Page width not found')
    quit()
  if image_gap is None:
    print('Note: Using default gap size')
    image_gap = 6;

  # Configure directory
  ensure_dir_exists(TEMP_DIR)
  temp_image_path = '{}/image.out'.format(TEMP_DIR)

  # Generate all images
  print('Generating images')
  bar = progress_bar_if_configured('Generating', len(requests))
  for request in requests:
    generate(request, requests[request], page_size, image_gap, bar)
  if bar is not None: bar.finish()