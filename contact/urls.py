from django.urls import path
from . import views


# URL configuration for contact app
# Maps contact-related routes to their corresponding views


urlpatterns = [

    # Endpoint for handling contact form submissions (AJAX POST request)
    path('contact_form', views.contact_form, name='contact_form'),

    # Route for rendering the contact page with form
    path('contact', views.contact, name='contact'),

]