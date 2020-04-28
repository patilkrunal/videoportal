from django.urls import path

from videoportal.views import (HomeView, NewVideo, VideoView, VideoFileView)

urlpatterns = [
    path('', HomeView.as_view(), name='video-home'),
    path('new_video', NewVideo.as_view(), name='video-new'),
    path('video/<int:id>/', VideoView.as_view(), name='video-detail'),
    path('get_video/<file_name>/', VideoFileView.as_view(), name='video-view'),
]
