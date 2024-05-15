from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.username


User.groups.field.remote_field.related_name = "custom_user_groups"
User.user_permissions.field.remote_field.related_name = "custom_user_permissions"


# site config
class SiteConfig(models.Model):
    open_ai_key = models.CharField(max_length=1000)
    open_ai_model = models.CharField(max_length=1000, blank=True, null=True)
    prompt = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.open_ai_model


# chat model
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_message = models.TextField(blank=True, null=True)
    ai_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
