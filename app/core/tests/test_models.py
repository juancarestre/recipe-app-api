from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'jcrestrepobedoya@gmail.com'
        password = 'TestJuan123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the for a new user is normalized"""
        email = 'test@MAYUSDOMAIN.COM'
        password = 'TestJuan123'
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test for error raises when a email is invalid"""
        password = 'TestJuan123'
        invalidEmails = [
            123,
            None,
            'plainaddress',
            '#@%^%#$@#$@#.com',
            '@example.com',
            'Joe Smith <email@example.com>',
            'email.example.com',
            'email@example@example.com',
            '.email@example.com',
            'email.@example.com',
            'email..email@example.com',
            'あいうえお@example.com',
            'email@example.com (Joe Smith)',
            'email@example',
            'email@-example.com',
            'email@example.web.',
            'email@example..com',
            'Abc..123@example.com',
            '”(),:;<>[\\]@example.com',
            'just”not”right@example.com',
            'this\\ is"really"not\\ allowed@example.com'
        ]

        for email in invalidEmails:
            with self.assertRaises(ValidationError):
                get_user_model().objects.create_user(email, password)

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@juan.com',
            'testJuan123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
