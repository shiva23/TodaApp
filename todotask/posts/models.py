from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
	tags = models.CharField(max_length=20)
	bookmarks= models.CharField(max_length=50)

	def __unicode__(self):
		return self.tags

	def __str__(self):
		return self.tags

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id":self.id})

