from django.shortcuts import render

from django.http import HttpRequest,Http404


def index(request):
    #story = get_story_so_far(index)
    context = {'story' : 'once upon a time there was a test',
                
                }

    return render(request, 'stories/index.html',context)
