import string, random
import os

from django.shortcuts import render
from django.views.generic.base import View, HttpResponseRedirect, HttpResponse
from .forms import NewVideoForm
from .models import Video

from django.core.files.storage import FileSystemStorage
from wsgiref.util import FileWrapper


class VideoFileView(View):
    def get(self, request, file_name):
        print('VideoFileView enter')
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file = FileWrapper(open(BASE_DIR + '/' + file_name, 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
        print('VideoFileView-get leave')
        return response


class HomeView(View):
    template_name = 'videoportal/index.html'

    def get(self, request):
        print('Homeview enter')
        # most_recent_videos = Video.objects.order_by('-datetime')[:8]
        most_recent_videos = Video.objects.all().order_by('-datetime')
        print('Homeview-get leave')
        return render(request, self.template_name,
                      {'menu_active_item': 'video-home', 'most_recent_videos': most_recent_videos})


class NewVideo(View):
    template_name = 'videoportal/new_video.html'

    def get(self, request):
        print('NewVideo-get enter')

        form = NewVideoForm()
        context = {
            'form': form
        }
        print('NewVideo-get leave')
        return render(request, self.template_name, context)

    def post(self, request):
        print('NewVideo-post enter')
        # pass filled out HTML-Form from View to NewVideoForm()
        form = NewVideoForm(request.POST, request.FILES)

        if form.is_valid():  # create a new Video Entry
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            video_id = form.cleaned_data['video_id']

            random_char = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            path = random_char + video_id

            new_video = Video(title=title, description=description, path=path, video_id=video_id)
            new_video.save()

            # redirect to detail view template of a Video
            print('NewVideo-post leave')
            return HttpResponseRedirect('video/{}'.format(new_video.id))
        else:
            return HttpResponse('Your form is not valid. Go back and try again.')


class VideoView(View):
    template_name = 'videoportal/video.html'

    def get(self, request, id):
        print('VideoView enter')
        video_by_id = Video.objects.get(id=id)  # fetch video from DB by ID
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        video_by_id.path = 'http://127.0.0.1:8000/get_video/' + video_by_id.path
        context = {'video': video_by_id}

        print('https://www.youtube.com/embed/' +  video_by_id.video_id )
        print('http://127.0.0.1:8000/post/' +  str(video_by_id.id) )
        print('VideoView-get leave')
        return render(request, self.template_name, context)