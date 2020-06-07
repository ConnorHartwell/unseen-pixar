from django.shortcuts import render

from django.http import HttpRequest,Http404
from .story import get_active_story

def index(request):
    story = get_active_story()
    if(story != None):
        context = {
                    'story' : story.once_upon_a_time,
                    'stage' : 'Once upon a time',
                    'story-id' : story.pk
                }
    else:
        context = {
            'story' : "Once upon a time, there was ..."
        }

    return render(request, 'stories/index.html',context)
