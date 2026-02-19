from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# AbstractModel

# İngilizce: Abstract model to store common fields for all models.
class AbstractModel(models.Model):


    # Auto-updated field whenever an object is updated
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',
        help_text='',
    )


    # Auto-created field at object creation
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',
        help_text='',
    )


    # Tells Django not to create a database table for this model
    class Meta:
        abstract = True



# GeneralSetting

class GeneralSetting(AbstractModel):

    name = models.CharField(
        default='',
        max_length=50,
        blank=True,  # Empty characters can be saved
        verbose_name='Name',
        help_text='This is variable of the setting',
    )

    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='',
    )

    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',
        help_text='',
    )


    # String representation for admin or shell
    def __str__(self):
        return f"General Setting: {self.name}"

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)



# ImageSetting

class ImageSetting(AbstractModel):

    name = models.CharField(
        default='',
        max_length=50,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting',
    )

    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='',
    )

    file = models.ImageField(
        default='',
        verbose_name='Image',
        help_text='',
        blank=True,
        upload_to='images/',
    )

    def __str__(self):
        return f"Image Setting: {self.name}"

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)



# Skill

class Skill(AbstractModel):

    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )

    name = models.CharField(
        default='',
        max_length=50,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting',
    )

    percen_tage = models.IntegerField(
        default=50,
        verbose_name='Percentage',
        validators=[MinValueValidator(0), MaxValueValidator(100)], 
        # Ensures value is between 0-100
    )

    def __str__(self):
        return f"Skill Setting: {self.name}"

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ('order',)



# Experience

class Experience(AbstractModel):

    company_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Company Name',
    )

    job_title = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Title',
    )

    job_location = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Location',
    )

    start_date = models.DateField(
        verbose_name='Start Date',
    )

    end_date = models.DateField(
        default=None,
        null=True,  # DB boş değer kabul eder
        blank=True, # Can be left blank in the form
        verbose_name='End Date',
    )

    def __str__(self):
        return f"Experience: {self.company_name}"

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experience'
        ordering = ('-start_date',)



# Education

class Education(AbstractModel):

    school_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='School Name',
    )

    major = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Major',
    )

    department = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Department',
    )

    start_date = models.DateField(
        verbose_name='Start Date',
    )

    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date',
    )

    def __str__(self):
        return f"Education: {self.school_name}"

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'
        ordering = ('-start_date',)



# SocialMedia

class SocialMedia(AbstractModel):

    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )

    link = models.URLField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Link',
    )

    icon = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Icon',
    )

    def __str__(self):
        return f"Social Media: {self.link}"

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Media'
        ordering = ('link',)



# Document

class Document(AbstractModel):

    order = models.IntegerField(
        default=0,
        verbose_name='Order'
    )

    slug = models.SlugField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Slug',
    )

    button_text = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Button Text',
    )

    file = models.FileField(
        default='',
        verbose_name='File',
        blank=True,
        upload_to='documents/'
    )

    def __str__(self):
        return f'Document: {self.slug}'

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Document'
        ordering = ('slug',)