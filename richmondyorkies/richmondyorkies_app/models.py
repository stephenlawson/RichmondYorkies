from tokenize import blank_re
from django.db import models


from unicodedata import category
from datetime import date

from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    message = models.CharField(max_length=2000, null=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Index(models.Model):
	about = RichTextUploadingField(null=True, blank=True)
	more_about = RichTextUploadingField(null=True, blank=True)

	def __str__(self):
		return self.about

class Dog(models.Model):
	headline = models.CharField(max_length=200)
	sub_headline = models.CharField(max_length=200, null=True, blank=True)
	thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="/images/placeholder.png")
	body = RichTextUploadingField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)
	featured = models.BooleanField(default=False)
	tags = models.ManyToManyField(Tag, null=True, blank=True)
	slug = models.SlugField(null=True, blank=True)
	link = models.CharField(null=True, blank=True, max_length=200)

	def __str__(self):
		return self.headline

	def save(self, *args, **kwargs):

		if self.slug == None:
			slug = slugify(self.headline)

			has_slug = Dog.objects.filter(slug=slug).exists()
			count = 1
			while has_slug:
				count += 1
				slug = slugify(self.headline) + '-' + str(count) 
				has_slug = Dog.objects.filter(slug=slug).exists()

			self.slug = slug

		super().save(*args, **kwargs)