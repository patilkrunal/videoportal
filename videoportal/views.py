import string, random
import os

from django.shortcuts import render
from django.views.generic.base import View, HttpResponseRedirect, HttpResponse
from .forms import NewVideoForm, CommentForm
from .models import Video, Comment

from django.core.files.storage import FileSystemStorage
from wsgiref.util import FileWrapper


class HomeView(View):
    template_name = 'videoportal/index.html'

    def get(self, request):
        # most_recent_videos = Video.objects.order_by('-datetime')[:8]
        most_recent_videos = Video.objects.all().order_by('-datetime')
        return render(request, self.template_name,
                      {'menu_active_item': 'home', 'most_recent_videos': most_recent_videos})


class NewVideo(View):
    template_name = 'videoportal/new_video.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/register')

        form = NewVideoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # pass filled out HTML-Form from View to NewVideoForm()
        form = NewVideoForm(request.POST, request.FILES)

        if form.is_valid():  # create a new Video Entry
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            file = form.cleaned_data['file']

            random_char = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            path = random_char + file.name

            fs = FileSystemStorage(location=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            # MYPATH = os.path.join(fs, 'media')
            filename = fs.save(path, file)
            file_url = fs.url(filename)

            print(fs)
            print(filename)
            print(file_url)

            new_video = Video(title=title, description=description, user=request.user, path=path)
            new_video.save()

            # redirect to detail view template of a Video
            return HttpResponseRedirect('video/{}'.format(new_video.id))
        else:
            return HttpResponse('Your form is not valid. Go back and try again.')


class VideoFileView(View):

    def get(self, request, file_name):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file = FileWrapper(open(BASE_DIR + '/' + file_name, 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
        return response


class VideoView(View):
    template_name = 'videoportal/video.html'

    def get(self, request, id):
        video_by_id = Video.objects.get(id=id)      # fetch video from DB by ID
        video_by_id.path = 'http://127.0.0.1:8000/get_video/' + video_by_id.path
        context = {'video': video_by_id}

        if request.user.is_authenticated:
            print('user signed in')
            comment_form = CommentForm()
            context['form'] = comment_form

        comments = Comment.objects.filter(video__id=id).order_by('-datetime')[:5]
        print(comments)
        context['comments'] = comments
        return render(request, self.template_name, context)


class CommentView(View):
    template_name = 'videoportal/comment.html'

    def post(self, request):
        form = CommentForm(request.POST)            # pass filled out HTML-Form from View to CommentForm()
        if form.is_valid():                         # create a Comment DB Entry
            text = form.cleaned_data['text']
            video_id = request.POST['video']
            video = Video.objects.get(id=video_id)

            new_comment = Comment(text=text, user=request.user, video=video)
            new_comment.save()
            # return HttpResponseRedirect('video/{}'.format(str(video_id)))
            return HttpResponseRedirect('video/{}'.format(video.id))
        return HttpResponse('This is Register view. POST Request.')