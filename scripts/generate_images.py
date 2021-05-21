#!/usr/bin/env python
import os
import subprocess
import re

print("Scanning for image requests")

posts = ['_posts/' + s for s in os.listdir('_posts')]
projects = ['_projects/' + s for s in os.listdir('_projects')]
files = posts + projects

START_KEY = '!@ generate_image '
END_KEY = '!@ end_generate'

requests = {}

for file in files:
  with open(file, 'r') as fh:
    all_lines = fh.readlines()

    engaged = False

    output = None
    inputs = []

    found = 0

    for line in all_lines:
      if line.startswith(START_KEY):
        output = line.replace(START_KEY, '').strip()
        engaged = True if len(output) > 3 else False
      elif line.startswith(END_KEY):
        if len(inputs) > 1:
          requests[output] = inputs
          found = found + 1
        engaged = False
        output = None
        inputs = []
      elif engaged:
        inputs.append(line.strip())

    if found > 0:
      print(' ', file, ':', found)

if len(requests) == 0:
  print('No requests found')
  quit()

print('Identifying page width')
page_size = None
image_gap = None
with open('assets/styles/main.css') as fh:
  all_lines = fh.readlines()
  width_check = re.compile('^.*--page-width: ([0-9]+)px;$')
  gap_check = re.compile('^.*\.photo \+ \.photo { margin-left: ([0-9]+)px; }$')

  for line in all_lines:
    width_match = width_check.match(line)
    if width_match is not None:
      page_size = int(width_match.group(1))
    gap_match = gap_check.match(line)
    if gap_match is not None:
      image_gap = int(gap_match.group(1))
if page_size is None:
  print('Page width not found')
  quit()
if image_gap is None:
  print('Using default gap size')
  image_gap = 6;

print('Generating images')

for request in requests:
  images = requests[request]
  num_images = len(images)

  widths = []
  heights = []

  for image in images:
    get_image_size = "identify -ping -format '%w %h' {}".format(image)
    image_size = subprocess.check_output(get_image_size, shell=True)
    [width, height] = image_size.decode('utf-8').split(' ')
    widths.append(width)
    heights.append(height)

  if len(set(widths)) != 1 or len(set(heights)) != 1:
    print('Skipping {}. Inconsistent image size'.format(request))

  gaps = len(images) - 1
  total_gap = image_gap * gaps
  displayed_image_size = (page_size - total_gap)/num_images
  true_image_size = widths[0]
  padding = round(int(true_image_size) / displayed_image_size * image_gap)
  generate_command = """
  convert \
    {source_images} \
    -background none \
    -splice {padding}x0+0+0 \
    +append \
    -chop {padding}x0+0+0 \
    {destination}
  """.format(**{
    'source_images': ' '.join(images),
    'padding': str(padding),
    'destination': request
  })

  print('  Generating', request)
  subprocess.run(generate_command, shell=True, check=True)