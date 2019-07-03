from django.contrib import admin
from django.urls import path, re_path

from boards import views
from pdfgen import views as pdf_views

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    re_path('boards/(?P<pk>\d+)/new', views.new_topic, name='new_topic'),
    re_path('boards/(?P<pk>\d+)/', views.board_topics, name='board_topics'),
    path('render/pdf', pdf_views.Pdf.as_view()),
=======
    # path('about', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    re_path('boards/(?P<pk>\d+)/new', views.new_topic, name='new_topic'),
    re_path('boards/(?P<pk>\d+)/', views.board_topics, name='board_topics'),
    re_path('input_data/(?P<pk>\d+)', views.input_data, name='input_data'),
>>>>>>> 1ee8b93e78e07f1a55b6b2c32acd37843cc2c7e8
    path('admin/', admin.site.urls),
]
