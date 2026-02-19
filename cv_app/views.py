from django.shortcuts import render, redirect, get_object_or_404
from cv_app.models import GeneralSetting, ImageSetting, Skill, Experience, Education, SocialMedia, Document


# Shared layout context generator
# Provides global template variables (settings, images, social links)

def layout(request):
    
    # Fetch all downloadable documents
    documents = Document.objects.all()

    # Retrieve general site settings from database
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_title').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameter
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').parameter
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameter
    home_banner_city = GeneralSetting.objects.get(name='home_banner_city').parameter
    about_myself_welcome = GeneralSetting.objects.get(name='about_myself_welcome').parameter
    about_myself_footer = GeneralSetting.objects.get(name='about_myself_footer').parameter

    # Retrieve image assets
    header_logo = ImageSetting.objects.get(name='header_logo').file
    home_banner_image = ImageSetting.objects.get(name='home_banner_image').file
    site_favicon = ImageSetting.objects.get(name='site_favicon').file

    # Retrieve social media links
    social_media = SocialMedia.objects.all()

    # Global template context
    context = {
        'documents': documents,
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'home_banner_city': home_banner_city,
        'about_myself_welcome': about_myself_welcome,
        'about_myself_footer': about_myself_footer,
        'home_banner_image': home_banner_image,
        'header_logo': header_logo,
        'site_favicon': site_favicon,
        'social_media': social_media,
    }

    return context



# Homepage view
# Renders main CV page with gallery, skills, experience, education

def index(request):

    # Retrieve homepage gallery images
    home_gallery_0 = ImageSetting.objects.get(name='home_gallery_0').file
    home_gallery_1 = ImageSetting.objects.get(name='home_gallery_1').file
    home_gallery_2 = ImageSetting.objects.get(name='home_gallery_2').file
    home_gallery_3 = ImageSetting.objects.get(name='home_gallery_3').file
    home_gallery_4 = ImageSetting.objects.get(name='home_gallery_4').file
    home_gallery_5 = ImageSetting.objects.get(name='home_gallery_5').file

    # Retrieve ordered skills (sorted by custom order field)
    skills = Skill.objects.all().order_by('order')

    # Retrieve professional experiences
    experiences = Experience.objects.all()

    # Retrieve education history
    educations = Education.objects.all()

    # Page-specific context
    context = {
        'home_gallery_0': home_gallery_0,
        'home_gallery_1': home_gallery_1,
        'home_gallery_2': home_gallery_2,
        'home_gallery_3': home_gallery_3,
        'home_gallery_4': home_gallery_4,
        'home_gallery_5': home_gallery_5,
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
    }

    return render(request, 'index.html', context=context)



# Dynamic document redirect view
# Retrieves document by slug and redirects to file URL

def redirect_urls(request, slug):

    # Fetch document or return 404 if not found
    document = get_object_or_404(Document, slug=slug)

    # Redirect user to the uploaded file URL
    return redirect(document.file.url)