from django.contrib import admin
from .models import User, SiteConfig, Chat

# Register your models here.
admin.site.register(User)

admin.site.register(SiteConfig)
admin.site.register(Chat)