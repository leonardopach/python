from pathlib import Path

from PIL import Image

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'fundo.jpg'
NEW_IMAGE = ROOT_FOLDER / 'new.jpg'


pil_image = Image.open(ORIGINAL)
print(pil_image.size)
width, height = pil_image.size
# exif = pil_image.info
# print(exif)

new_width = 640
new_height = round(height * new_width / width)
print(new_width, new_height)
print(width, height)

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(NEW_IMAGE,
               optimize=True,
               quality=50)
