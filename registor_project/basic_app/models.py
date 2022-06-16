from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # creating one to one relationship with already existing model User
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)

    # Adding additional attributies
    portfolio = models.URLField(blank=True)
    picture = models.URLField(blank=True)

    # just to return name as a string
    def __str__(self):
        return self.user.username

class URLinput(models.Model):
    Enter_URL = models.URLField()
