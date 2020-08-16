from . import views
from django.urls import path

urlpatterns = [
	path('', views.BlogPostList.as_view(), name='home'),
	path('<slug:slug>/', views.BlogPostDetail.as_view(), name='post_detail'),
]
