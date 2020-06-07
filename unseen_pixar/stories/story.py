from .models import *
import random

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
    current_story = Story.objects.get(pk=storyid)
