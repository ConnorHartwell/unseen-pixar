from django.db import models

#base story
#everything length of a tweet?
#i assume we need to keep track user has added what item, maybe a model for a text field.
#storyid - genre - ouat - everyday - oneday - result - result2 - fin


#genre - each story must have a genre. can be a concept instead of a genre. helps the user get imagination flowing.
#genreid - description
class Genre(models.Model):
    description = models.CharField(max_length=300)
    
class Story(models.Model):
    genre = models.ForeignKey(Genre, on_delete = models.PROTECT)
    once_upon_a_time = models.CharField(max_length=280)
    every_day = models.CharField(max_length=280)
    one_day = models.CharField(max_length=280)
    result = models.CharField(max_length=280)
    result2 = models.CharField(max_length=280)
    until_finally = models.CharField(max_length=280)

#usertable
#userid - username - email
class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=100) #obviously this needs actual encryption - there's apps to do this for me though later.

#userstories - stops users from working on same story twice, and can track when a user's story is complete.
#represents the many-many relationship between user and stories
#userid - storyid
class UserStory(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    story = models.ForeignKey(Story, on_delete=models.SET_NULL, null = True)

# Create your models here.
