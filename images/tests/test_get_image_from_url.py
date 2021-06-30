from django.test import TestCase

from images.services import get_image_from_url


class ImageFromUrlTestCase(TestCase):
    def test_getting_image_from_url(self):
        image_url = "https://upload.wikimedia.org/wikipedia/commons/c/cd/Google_Logo_%281998%29.png"
        image, name = get_image_from_url(image_url)
        self.assertIsNotNone(image)
        self.assertEqual(name, "Google_Logo_%281998%29.png")
