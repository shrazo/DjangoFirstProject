from django.contrib import admin
from .models import Board, Topic, Post, Contact


# Register your models here.
admin.site.register(Board) 
admin.site.register(Topic) 
admin.site.register(Post) 
admin.site.register(Contact) 