from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class ClientUser(User):
    place = models.CharField(max_length=50)

