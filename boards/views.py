from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Board, Topic, Post
from .forms import NewTopicForm, ContactForm
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()

    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)
    else:
        form = NewTopicForm()
    
    return render(request, 'new_topic2.html', {'board':board, 'form':form})


# def new_topic2(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     user = User.objects.first()

#     if request.method == 'POST':
#         form = NewTopicForm(request.POST)
#         if form.is_valid():
#             topic = form.save(commit=False)
#             topic.board = board
#             topic.starter = user
#             topic.save()
#             post = Post.objects.create(
#                 message = form.cleaned_data.get('message'),
#                 topic = topic,
#                 created_by = user,
#             )
#             return redirect('board_topics', pk=board.pk)
#     else:
#         form = NewTopicForm()

#     return render(request, 'new_topic.html', {'board': board, 'form':form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return render(request, 'mess_sent_success.html')
    else:
        form = ContactForm(request.POST)
    return render(request, 'contact.html', {'form': form})

def input_data(request, pk):
    return render(request, 'excel.html', {'N':range(1, int(pk)+1)})