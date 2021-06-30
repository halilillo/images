from io import BytesIO

from django.core.files.base import File
from django.test import TestCase
from PIL import Image as PILImage

from images.models import Image
from images.services import resize_image


class ResizeImageTestCase(TestCase):
    def setUp(self):
        test_image = self.get_image_file()
        Image.objects.create(source=test_image)

    @staticmethod
    def get_image_file(name="test.png", ext="png", size=(50, 50), color=(256, 0, 0)):
        file_obj = BytesIO()
        image = PILImage.new("RGB", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)

    def test_resize_image(self):
        image = Image.objects.first()
        resized_image = resize_image(image.source, 40, 40)
        self.assertEqual(resized_image.size, (40, 40))
