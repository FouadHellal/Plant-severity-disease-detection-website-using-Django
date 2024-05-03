from django.urls import path
from .views import upload_image,chat_view,about

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
    path('chat/', chat_view, name='chat'),
    path('about/', about, name='about'),
]
