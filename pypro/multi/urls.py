from django.urls import path

from pypro.multi.views import video

app_name = 'multi'
urlpatterns = [
    path('<slug:slug>', video, name='video')
]