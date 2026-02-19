from django.contrib import admin
from cv_app.models import *


# DJANGO ADMIN CONFIGURATION

# This file customizes how models appear and behave
# inside Django’s built-in admin panel.
#
# Each @admin.register decorator registers the model
# and attaches a customized ModelAdmin configuration.




# GENERAL SETTING ADMIN

@admin.register(GeneralSetting)
class GeneralSettingsAdmin(admin.ModelAdmin):
    """
    Admin configuration for GeneralSetting model.
    Controls how site-wide key/value configurations
    are managed from the Django admin panel.
    """

    # Fields displayed as columns in admin list view
    list_display = [
        'id',
        'name',
        'description',
        'parameter',
        'updated_date',
        'created_date'
    ]

    # Enables search functionality in admin panel
    # Allows searching by these fields
    search_fields = ['name', 'description', 'parameter']

    # Makes selected fields editable directly from list view
    # NOTE: These fields must also exist in list_display
    list_editable = ['description', 'parameter']

    class Meta:
        model = GeneralSetting



# IMAGE SETTING ADMIN

@admin.register(ImageSetting)
class ImageSettingsAdmin(admin.ModelAdmin):
    """
    Admin configuration for ImageSetting model.
    Used for managing images such as logos,
    banners, or profile pictures.
    """

    list_display = [
        'id',
        'name',
        'description',
        'file',
        'updated_date',
        'created_date'
    ]

    search_fields = ['name', 'description', 'file']

    list_editable = ['description', 'file']

    class Meta:
        model = ImageSetting



# SKILL ADMIN

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """
    Admin configuration for Skill model.
    Represents technical or personal skills
    displayed on the CV page.
    """

    list_display = [
        'id',
        'order',
        'name',
        'percen_tage',
        'updated_date',
        'created_date'
    ]

    # Enables quick search by skill name
    search_fields = ['name']

    # Allows inline editing for ordering and percentage
    list_editable = ['order', 'name', 'percen_tage']

    class Meta:
        model = Skill



# EXPERIENCE ADMIN

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """
    Admin configuration for Experience model.
    Stores professional work experiences.
    """

    list_display = [
        'id',
        'company_name',
        'job_title',
        'job_location',
        'start_date',
        'end_date',
        'updated_date',
        'created_date'
    ]

    search_fields = ['company_name', 'job_title', 'job_location']

    list_editable = [
        'company_name',
        'job_title',
        'job_location',
        'start_date',
        'end_date',
    ]

    class Meta:
        model = Experience



# EDUCATION ADMIN

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """
    Admin configuration for Education model.
    Manages academic background information.
    """

    list_display = [
        'id',
        'school_name',
        'major',
        'department',
        'start_date',
        'end_date',
        'updated_date',
        'created_date'
    ]

    search_fields = ['school_name', 'major', 'department']

    list_editable = [
        'school_name',
        'major',
        'department',
        'start_date',
        'end_date',
    ]

    class Meta:
        model = Education



# SOCIAL MEDIA ADMIN

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    """
    Admin configuration for SocialMedia model.
    Used to manage social platform links and icons.
    """

    list_display = [
        'id',
        'order',
        'link',
        'icon',
        'updated_date',
        'created_date'
    ]

    search_fields = ['link', 'icon']

    list_editable = ['order', 'link', 'icon']

    class Meta:
        model = SocialMedia



# DOCUMENT ADMIN

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """
    Admin configuration for Document model.
    Handles downloadable files such as CV PDFs
    or portfolio documents.
    """

    list_display = [
        'id',
        'order',
        'slug',
        'button_text',
        'file',
        'updated_date',
        'created_date'
    ]

    # Enables quick search by slug or button text
    search_fields = ['slug', 'button_text']

    list_editable = ['order', 'slug', 'button_text', 'file']

    class Meta:
        model = Document