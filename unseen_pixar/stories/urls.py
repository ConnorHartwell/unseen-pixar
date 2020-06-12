from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('story/<int:storyid>/<int:stageid>', views.get_story_from_id, name = 'story'),
]