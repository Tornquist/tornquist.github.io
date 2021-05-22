import subprocess

class ImageMagick():
  def generate(images, padding, destination):
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
      'destination': destination
    })
    subprocess.run(generate_command, shell=True, check=True)

  def compare(a, b):
    compare_command = "compare -metric AE {} {} null: 2>&1".format(a, b)
    subprocess.run(compare_command, capture_output=True, shell=True, check=True)

  def check_same_size(images):
    widths = []
    heights = []

    for image in images:
      get_image_size = "identify -ping -format '%w %h' {}".format(image)
      image_size = subprocess.check_output(get_image_size, shell=True)
      [width, height] = image_size.decode('utf-8').split(' ')
      widths.append(width)
      heights.append(height)

    one_size = len(set(widths)) == 1 and len(set(heights)) == 1

    return one_size, (widths[0], heights[0])