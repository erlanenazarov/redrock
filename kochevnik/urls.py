"""kochevnik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from kochevnik import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'things_todo/$', 'base.views.things_to_do'),
    url(r'trip_planner/$', 'main.views.tripplaner'),
    url(r'post_planner/$', 'main.views.post_planner'),
    url(r'things_to_do/(?P<things_id>\d+)/$', 'base.views.things_one'),
    url(r'tours/$', 'base.views.tours'),
    url(r'submit/$', 'main.views.post_faq'),
    url(r'contacts/$', 'base.views.contacts'),
    url(r'about_us/$', 'about_us.views.about'),
    url(r'tours/category/(?P<category_id>\d+)/$', 'base.views.tours_by_category'),
    url(r'tour/(?P<tour_id>\d+)/$', 'base.views.tour'),
    url(r'gallery/$', 'media.views.gallery'),
    url(r'blog/$','blog.views.blog'),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'$', 'base.views.index'),
]
