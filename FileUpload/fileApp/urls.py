
from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name="home")
# ]

urlpatterns = [
    path('', views.upload_and_display_files, name='upload_and_display'),
]