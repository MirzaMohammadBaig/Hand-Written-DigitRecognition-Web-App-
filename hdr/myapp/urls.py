from pydoc import visiblename
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name ='index'),
    path('login', views.login, name='login'),
    path('run', views.recognize, name='recognize'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
