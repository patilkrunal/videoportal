from django.urls import path

from videoportal.views import (VideoListView, VideoDetailView, VideoFileView)

urlpatterns = [
    path('', VideoListView.as_view(), name='video-home'),
    path('video/<int:id>/', VideoDetailView.as_view(), name='video-detail'),
    path('get_video/<file_name>/', VideoFileView.as_view(), name='video-view'),
]
