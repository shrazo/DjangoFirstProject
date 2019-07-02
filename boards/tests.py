from django.shortcuts import render, reverse
from django.urls import resolve
from django.test import TestCase
from .views import home, new_topic
from .models import Board

# Create your tests here.
class HomeTests(TestCase):
	def test_home_view_status_code(self):
		url = reverse('home') 
		response = self.client.get(url) 
		self.assertEquals(response.status_code, 200) 

	def test_home_url_resolves_home_view(self):
		view = resolve('/') 
		self.assertEquals(view.func, home)


class NewTopicTests(TestCase):

	def setUp(self):
		Board.objects.create(name='Django', description='Django boards')
	
	def test_new_topic_view_success_status_code(self):
		url = reverse('new_topic', kwargs={'pk':1})
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	def test_new_topic_view_not_found_status_code(self):
		url = reverse('new_topic', kwargs={'pk':99})
		response = self.client.get(url)
		self.assertEquals(response.status_code, 404)
	
	def test_new_topic_view_contains_link_back_to_board_topics_view(self):
		new_topic_url = reverse('new_topic', kwargs={'pk':1})
		board_topics_url = reverse('board_topics', kwargs={'pk':1})
		response = self.client.get(new_topic_url)
		self.assertContains(response, 'href="{0}"'.format(board_topics_url))
	
	def test_new_topic_url_resolves_new_topic_view(self):
		view = resolve('/boards/1/new')
		self.assertEquals(view.func, new_topic)