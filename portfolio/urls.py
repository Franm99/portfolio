from django.urls import path

from .views import home, about, projects, contact

app_name = 'portfolio'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('projects/', projects, name='projects'),
]