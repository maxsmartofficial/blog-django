from django.db import models
from django.contrib.auth.models import User
# Create your models here.

PUBLISHED = (
	(0, 'Draft'),
	(1, 'Published')
)


class BlogPost(models.Model):

	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, unique=True)
	author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='blog_posts')
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	content = models.TextField()
	status = models.IntegerField(choices=PUBLISHED, default=0)

	class Meta:
		# Order by latest created
		ordering = ['-created_on']

	def __str__(self):
		# Use the title as the string representation
		return(self.title)
