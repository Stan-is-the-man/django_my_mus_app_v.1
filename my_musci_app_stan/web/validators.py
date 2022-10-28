from django.core.exceptions import ValidationError


def user_name_isalnum(value):

    if not value.isalnum() and not value == '_':
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


