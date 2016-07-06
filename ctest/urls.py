from django.conf.urls import url

from . import views

# app_name = 'ctest'
urlpatterns = [
    url(r'^$', views.chatroom, name = 'chatroom'),
]
