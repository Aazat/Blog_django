"""Defines url patterns for learning logs"""
from django.urls import path
from . import views
app_name= 'learning_logs'
urlpatterns= [
	path('',views.index, name='index'),	# Home page
	path('topics/',views.topics, name='topics'),	# Topics Page
	path('topics/<int:topic_id>/',views.topic, name='topic')	# Individual Topic Page
]