from django.contrib import admin
from django.urls import path, re_path

from boards import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('about', views.about, name='about'),
    re_path('boards/(?P<pk>\d+)/new', views.new_topic, name='new_topic'),
    re_path('boards/(?P<pk>\d+)/', views.board_topics, name='board_topics'),
    path('admin/', admin.site.urls),
]
