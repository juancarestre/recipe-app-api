from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def emailValidator(email):
    '''Checks if an email is valid'''
    try:
        validate_email(str(email))
    except ValidationError:
        raise ValidationError(f'{email} is not a valid email')