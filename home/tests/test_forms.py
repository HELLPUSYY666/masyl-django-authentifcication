from django.test import TestCase
from authentication.models import User
from home.models import Masyli, SupernaturalAbilities
from home.forms import MasyliConfirmDelete, MasyliForm, SupernaturalForm, RegisterForm
from django.core.files.uploadedfile import SimpleUploadedFile


class MasyliConfirmDeleteTest(TestCase):
    def test_confirm_delete_valid(self):
        form = MasyliConfirmDelete(data={'confirm_delete': True})
        self.assertTrue(form.is_valid())

    def test_confirm_delete_invalid(self):
        form = MasyliConfirmDelete(data={'confirm_delete': False})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['__all__'], ['You must confirm this form!'])


class MasyliFormTest(TestCase):
    def test_masyli_form_valid(self):
        photo = SimpleUploadedFile("test_image.jpg", b"image_content", content_type="image/jpeg")
        form = MasyliForm(data={
            'name': 'Test Masyli',
            'age': 10,
            'color': 'Red',
            'origin': 'Unknown',
        }, files={'photo': photo})
        self.assertTrue(form.is_valid())

    def test_masyli_form_invalid(self):
        form = MasyliForm(data={
            'name': '',
            'age': '',
            'color': '',
            'origin': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('age', form.errors)
        self.assertIn('color', form.errors)
        self.assertIn('origin', form.errors)


class SupernaturalFormTest(TestCase):
    def setUp(self):
        self.masyli = Masyli.objects.create(
            name="Test Masyli",
            age=10,
            color="Blue",
            origin="Unknown",
            photo=SimpleUploadedFile("test_image.jpg", b"image_content", content_type="image/jpeg")
        )

    def test_supernatural_form_valid(self):
        photo = SimpleUploadedFile("test_image.jpg", b"image_content", content_type="image/jpeg")
        form = SupernaturalForm(data={
            'masyli': self.masyli.id,
            'ability_name': 'Invisibility',
            'description': 'Can become invisible at will.',
        }, files={'photo': photo})
        self.assertTrue(form.is_valid())

    def test_supernatural_form_invalid(self):
        form = SupernaturalForm(data={
            'masyli': '',
            'ability_name': '',
            'description': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('masyli', form.errors)
        self.assertIn('ability_name', form.errors)
        self.assertIn('description', form.errors)
