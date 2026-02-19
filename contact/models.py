from django.db import models
from cv_app.models import AbstractModel


# Message Model
# Stores contact form submissions in the database
# Inherits created_date and updated_date from AbstractModel

class Message(AbstractModel):
    
    # Sender's full name
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
    )

    # Sender's email address
    email = models.EmailField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='E-mail',
    )

    # Message subject line
    subject = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Subject',
    )

    # Main message content
    message = models.TextField(
        default='',
        blank=True,
        verbose_name='Message',
    )

    # String representation in admin panel
    def __str__(self):
        return f'Message: {self.name}'
    
    class Meta:
        # Human-readable model names in Django admin
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

        # Default ordering (alphabetical by name)
        ordering = ('name',)