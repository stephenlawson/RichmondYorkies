from django.contrib import admin

# Register your models here.

from .models import Contact, Dog, Tag, Index

admin.site.register(Contact)
admin.site.register(Dog)
admin.site.register(Tag)
admin.site.register(Index)