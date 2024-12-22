# apps/account/models

# Django modules
from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar')
    instagram = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
    	verbose_name_plural = 'Profiles'

    def __str__(self):
    	return self.user.username

    def get_absolute_url(self):
        return reverse(
            'blog:posts_by_user_view',
            kwargs={
                "user_slug": self.slug,
            }
        )