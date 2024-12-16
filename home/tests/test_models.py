from django.test import TestCase
from home.models import Masyli, SupernaturalAbilities
from django.core.files.uploadedfile import SimpleUploadedFile


class MasyliModelTest(TestCase):
    def setUp(self):
        self.masyli = Masyli.objects.create(
            name="Zardak",
            age=120,
            color="Red",
            origin="Unknown Planet",
            opasnosti=Masyli.OPAS,
            photo=SimpleUploadedFile(name='test_image.jpg', content=b'some_image_data', content_type='image/jpeg')
        )

    def test_masyli_creation(self):
        self.assertEqual(self.masyli.name, "Zardak")
        self.assertEqual(self.masyli.age, 120)
        self.assertEqual(self.masyli.color, "Red")
        self.assertEqual(self.masyli.origin, "Unknown Planet")
        self.assertEqual(self.masyli.opasnosti, Masyli.OPAS)
        self.assertIsNotNone(self.masyli.photo)

    def test_str_representation(self):
        self.assertEqual(str(self.masyli), "Zardak")
