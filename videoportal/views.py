import os
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View, HttpResponse
from .models import Video
from wsgiref.util import FileWrapper


def home(request):
    context = {
        'recent_videos': Video.objects.all()
    }
    return render(request, 'videoportal/home.html', context)


class VideoListView(ListView):
    model = Video
    template_name = 'videoportal/home.html'
    context_object_name = 'recent_videos'
    ordering = ['-datetime']
    paginate_by = 5


class VideoDetailView(View):
    template_name = 'videoportal/video_detail.html'

    def get(self, request, id):
        print('VideoDetailView enter')
        video_by_id = Video.objects.get(id=id)  # fetch video from DB by ID
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        video_by_id.path = 'http://127.0.0.1:8000/get_video/' + video_by_id.path
        context = {'video': video_by_id}

        # print('https://www.youtube.com/embed/' + video_by_id.video_id)
        # print('http://127.0.0.1:8000/post/' + str(video_by_id.id))
        print('VideoDetailView-get leave')
        return render(request, self.template_name, context)


class VideoFileView(View):
    def get(self, request, file_name):
        print('VideoFileView enter')
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file = FileWrapper(open(BASE_DIR + '/' + file_name, 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
        print('VideoFileView-get leave')
        return response
