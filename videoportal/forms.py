from django import forms


class NewVideoForm(forms.Form):
    title = forms.CharField(label='Title', max_length=20)
    description = forms.CharField(label='Description', max_length=300)
    video_id = forms.CharField(label='video_id', max_length=20)