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


class SupernaturalAbilitiesModelTest(TestCase):
    def setUp(self):
        self.masyli = Masyli.objects.create(
            name="Zardak",
            age=120,
            color="Red",
            origin="Unknown Planet",
            opasnosti=Masyli.OPAS,
            photo=SimpleUploadedFile(name='test_image.jpg', content=b'some_image_data', content_type='image/jpeg')
        )
        self.ability = SupernaturalAbilities.objects.create(
            masyli=self.masyli,
            ability_name="Fire Breathing",
            description="Can breathe fire up to 20 meters.",
            photo=SimpleUploadedFile(name='ability_image.jpg', content=b'some_image_data', content_type='image/jpeg')
        )

    def test_supernatural_ability_creation(self):
        self.assertEqual(self.ability.masyli, self.masyli)
        self.assertEqual(self.ability.ability_name, "Fire Breathing")
        self.assertEqual(self.ability.description, "Can breathe fire up to 20 meters.")
        self.assertIsNotNone(self.ability.photo)

    def test_str_representation(self):
        self.assertEqual(str(self.ability), "Fire Breathing")

    def test_cascade_deletion(self):
        self.masyli.delete()
        self.assertFalse(SupernaturalAbilities.objects.filter(id=self.ability.id).exists())
