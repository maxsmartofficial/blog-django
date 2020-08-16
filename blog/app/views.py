from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import BlogPost

# Create your views here.
class BlogPostList(generic.ListView):
	queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
	template_name = 'index.html'

class BlogPostDetail(generic.DetailView):
	model = BlogPost
	template_name = 'post_detail.html'
