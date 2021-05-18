from task import views
from django.urls import path

urlpatterns = [
    path('', views.create),
    path('<str:audioFileType>/<int:audio_ID>', views.router),
    path('<str:audioFileType>', views.verify)
]
