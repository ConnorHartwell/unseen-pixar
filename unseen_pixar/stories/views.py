from django.shortcuts import render

from django.http import Http404, HttpRequest, HttpResponse
from .story import *
from django.template import Context

def index(request):
    story = get_active_story()
    if(story != None):
        context = {
                    'this_story' : story,
                    'stageid' : '0',
                }
    else:
        context = {
            'stage' : '',
            'story' : "Once upon a time, there was ..."
        }

    return render(request, 'stories/index.html',context)

def get_story_from_id(request, storyid, stageid):
    content = {
        'story' : get_curr_story_text(storyid, stageid),
        'stage' : stage_id_to_string(stageid)
    }
    return render(request, 'stories/index.html',content)
