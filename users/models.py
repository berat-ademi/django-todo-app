from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, default='profile_pics/default.jpg')

    @property
    def picture_url(self):
        if self.profile_picture:
            return self.profile_picture.url
        return '/media/profile_pics/default.jpg'