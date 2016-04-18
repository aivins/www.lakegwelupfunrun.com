
import sys

html = """
<div class="sponsors-logo col-lg-3 com-md-3 col-sm-3 col-xs-6">
  <a target="_blank" href="{}">
    <img src="/images/{}" alt="{}" title="{}">
  </a>
</div>
"""

for line in sys.stdin:
    (name, url, image) = line.split(',')
    name = name.strip()
    url = url.strip()
    image = image.strip()

    if image == "":
        image = "empty_gallery.png"

    print(html.format(url, image, name, name))
