# apps/account/models

# Django modules
from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.urls import reverse

# Third party modules
from tinymce import models as tinymce_models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar')
    instagram = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    info = tinymce_models.HTMLField(blank=True, null=True)

    class Meta:
    	verbose_name_plural = 'Profiles'

    def __str__(self):
    	return self.user.username

    def get_all_posts_url(self):
        return reverse(
            'blog:posts_by_user_view',
            kwargs={
                "user_slug": self.slug,
            }
        )

    def get_profile_edit_url(self):
        return reverse(
            'account:profile_edit_view'
        )