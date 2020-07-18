from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('', views.index, name='home'),
    path('field', views.field, name='field'),
    path('e.next', views.content, name='content'),

    path('bee', views.fe_bee, name='fe_bee'),
    path('bee_unit1', views.bee_unit1, name='bee_unit1'),
    path('bee_unit2', views.bee_unit2, name='bee_unit2'),
    path('bee_unit3', views.bee_unit3, name='bee_unit3'),
    path('bee_unit4', views.bee_unit4, name='bee_unit4'),
    path('bee_unit5', views.bee_unit5, name='bee_unit5'),
    path('bee_unit6', views.bee_unit6, name='bee_unit6'),

    path('ec', views.fe_ec, name='fe_ec'),
    path('ec_unit1', views.ec_unit1, name='ec_unit1'),
    path('ec_unit3', views.ec_unit3, name='ec_unit3'),
    path('ec_unit4', views.ec_unit4, name='ec_unit4'),
    path('ec_unit5', views.ec_unit5, name='ec_unit5'),
    path('ec_unit6', views.ec_unit6, name='ec_unit6'),

    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('technical', views.technical, name='technical')

]
