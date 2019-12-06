from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',test,name="home"),
    path('data/',vincode_data,name="vincode_data"),
    path('about/',about,name="about"),
    path('contact/',contact,name="contact"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)