from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('<int:pk>',views.get_story_from_id, name = 'findstory')
]