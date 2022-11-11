from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',about,name='home'),
    path('teachers/',teachers,name='teachers'),
    path('ed/',Standarts.as_view(), name='ed'),
    path('teachers/<slug:post_slug>/',teacher_post,name='post'),
    path('ed/<slug:ed_slug>/',area_post,name='ed'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
