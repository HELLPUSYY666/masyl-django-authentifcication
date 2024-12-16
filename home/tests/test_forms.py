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
            'age': -5,
            'color': '',
            'origin': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('age', form.errors)
