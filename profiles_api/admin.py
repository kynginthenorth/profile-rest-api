from django.contrib import admin

from profiles_api import models


admin.site.register(models.UserProfiles)
admin.site.register(models.ProfileFeedItem)
