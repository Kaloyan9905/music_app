from django.core.exceptions import ValidationError


def username_validator(value):
    for char in value:
        if not char.isalnum() and not char == '_':
            raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')
