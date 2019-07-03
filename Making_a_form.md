1. First create a url pattern to catch the url that create a form like 
    urlpatterns = [
        ...
        re_path('boards/(?P<pk>\d+)/new', views.new_topic, name='new_topic'),
        ...
    ]

2. Then create a view as you used in the urlpatterns and assign a template for the view like as shown below:
    
    def new_topic(request, pk):
    return render(request, 'new_topic.html')

    Here new_topic.html is the html template
3. 