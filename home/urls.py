from django.contrib import admin
from django.urls import include, path

from home import views

#django admistration dasboard
admin.site.site_header="Developer  Jeevan "
admin.site.site_title="welcome to Jeevan's Dashboard"
admin.site.index_title='Welcome to this portal'

urlpatterns = [
     path('', views.home, name='home'),
     path('about', views.about, name='about'),
     path('contact', views.contact_form, name='contact'),
     path('project', views.project, name='project')

]
