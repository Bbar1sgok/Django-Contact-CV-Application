from django.urls import path
from . import views

# Application URL configuration for cv_app
# Maps incoming requests to corresponding view functions

urlpatterns = [

    # Root URL → renders homepage (index view)
    path('', views.index, name='index'),

    # Dynamic slug URL → captures slug value and passes to redirect_urls view
    # Used for document redirection or dynamic content handling
    path('<slug:slug>/', views.redirect_urls, name='redirect_urls'),

]