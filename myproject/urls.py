from django.contrib import admin
from django.urls import path, re_path

from boards import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('about', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    re_path('boards/(?P<pk>\d+)/new', views.new_topic, name='new_topic'),
    re_path('boards/(?P<pk>\d+)/', views.board_topics, name='board_topics'),
    re_path('input_data/(?P<pk>\d+)', views.input_data, name='input_data'),
    path('admin/', admin.site.urls),
]
