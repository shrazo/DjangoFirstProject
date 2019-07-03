from django.contrib import admin
from django.urls import path, re_path

from boards import views
from pdfgen import views as pdf_views

urlpatterns = [
    path('', views.home, name='home'),
    re_path('boards/(?P<pk>\d+)/new', views.new_topic, name='new_topic'),
    re_path('boards/(?P<pk>\d+)/', views.board_topics, name='board_topics'),
    path('render/pdf', pdf_views.Pdf.as_view()),
    path('admin/', admin.site.urls),
]
