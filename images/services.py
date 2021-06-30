import base64
import tempfile
from io import BytesIO

import requests
from PIL import Image


def get_image_from_url(url):
    response = requests.get(url, stream=True)

    if response.status_code != requests.codes.ok:
        return

    file_name = url.split("/")[-1]

    image = tempfile.NamedTemporaryFile()

    for block in response.iter_content(1024 * 8):

        if not block:
            break
        image.write(block)

    return image, file_name


def resize_image(original_image, width=None, height=None):
    w = original_image.width
    h = original_image.height

    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)

    image = Image.open(original_image.path)

    image.thumbnail(max_size, Image.ANTIALIAS)

    return image


def image_to_base64(image):
    output_buffer = BytesIO()
    image.save(output_buffer, format=image.format)
    byte_data = output_buffer.getvalue()
    base64_str = (
        f"data:image/{image.format};base64," + base64.b64encode(byte_data).decode()
    )

    return base64_str
