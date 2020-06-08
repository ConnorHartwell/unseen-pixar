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

def get_story_from_id(request, storyid):
    content = Context({
        'story' : Story.objects.get(pk=storyid),
        'stage' : 0,
    })
    return render(request, 'stories/base.html',content)

def get_curr_story_text(storyid, stageid):
    return HttpResponse(get_curr_story_text(storyid,stageid))

def get_curr_story_header(stageid):
    return HttpResponse(stage_id_to_string(stageid))
