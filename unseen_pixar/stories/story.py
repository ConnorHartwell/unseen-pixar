from .models import *
import random
from django.http import HttpResponse

stages = ['Once upon a time', 'Each day', 'One day', 'Because of this', 'Because of this','Until Finally']


#get random active story 
def get_active_story():

    active_stories = Story.objects.filter(until_finally__isnull=False) #take out all story objects with final part filled
    if(active_stories.count() > 0):
        return active_stories[random.randint(0,active_stories.count()-1)]
    else:
        return None

#start new story
def create_story(intro):
    new_story = Story(ouat=intro)
    
    new_story.save()

def add_to_story(storyid, text):
    current_story =load_story(storyid)

def next_part_of_story(storyid,stageid):
    stageid += 1
    this_story = load_story(storyid)

    return this_story[stageid]
    
#REFACTOR LATER - this is inefficient. as in the whole pipeline of doing this
def load_story(storyid):
    this_story = Story.objects.get(pk=storyid)
    
    currstory = []
    try:
        currstory[0]=this_story.once_upon_a_time;
        currstory[1]=this_story.every_day
        currstory[2]=this_story.one_day;
        currstory[3]=this_story.result
        currstory[4]=this_story.result2
        currstory[5]=this_story.until_finally;
    except TypeError:
        return currstory
    return currstory

def stage_id_to_string(stageid):
    return stages[stageid]
