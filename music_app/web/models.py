from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from music_app.web.validators import username_validator


class Profile(models.Model):
    MAX_USERNAME_LEN = 15
    MIN_USERNAME_LEN = 2

    username = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_USERNAME_LEN,
        validators=(
            username_validator,
            MinLengthValidator(MIN_USERNAME_LEN),
        ),
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    MAX_NAME_LEN = 30
    MIN_PRICE = 0

    MUSIC_CHOICES = (
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'),
    )

    album_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=MAX_NAME_LEN,
    )

    artist = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_NAME_LEN,
    )

    genre = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_NAME_LEN,
        choices=MUSIC_CHOICES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(MIN_PRICE)
        ],
    )
