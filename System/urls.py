from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^success', views.index, name='success'),
    url(r'^register/rent', views.rent_setup, name='Rent')
]
