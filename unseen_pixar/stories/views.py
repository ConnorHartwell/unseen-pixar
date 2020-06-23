from django.shortcuts import render

from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from .story import *
from django.template import Context
from django.urls import reverse
import urllib

def index(request):
    story = get_active_story()
    if(story != None):
        context = {
                    'story' : story,
                    'stage' : 0,
                }
    else:
        context = {
            'stage' : 0,
            'story' : create_story()
        }

    return render(request, 'stories/index.html',context)

def get_story_from_id(request,stageid,storyid):
    if(request.method == "GET"):
        content = {
            'story' : get_curr_story_text(storyid, stageid),
            'stage' : stage_id_to_string(stageid),
            'is_last': is_last_section(storyid,stageid)
        }
        return JsonResponse(content)
    return 0
    
def submit(request,storyid):
    try:
        new_text = request.POST['story_text']
    except(Story.DoesNotExist):
        return index(request)
    else:
        add_to_story(storyid,new_text)
    return HttpResponseRedirect(reverse('index'))
