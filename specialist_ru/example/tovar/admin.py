from django.contrib import admin

# Register your models here.
from .models import Tovar, Tag, Group

admin.site.register(Tovar)
admin.site.register(Tag)
admin.site.register(Group)