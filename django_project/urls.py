from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from videoportal.views import VideoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('blog.urls', 'blog'), namespace='blog')),
    path('videoportal/', include(('videoportal.urls', 'videoportal'), namespace='videoportal')),
    path('video/<int:id>', VideoView.as_view(), name='video-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)