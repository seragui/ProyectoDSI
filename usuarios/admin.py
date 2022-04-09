from django.contrib import admin
from usuarios import models

# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)