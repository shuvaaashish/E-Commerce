from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction_listings(models.Model):
    title=models.CharField(max_length=64)
    Owner=models.ForeignKey(User, on_delete=models.CASCADE , related_name="seller")
    description=models.CharField(max_length=350)

class Bids(models.Model):
    pass

class Comments(models.Model):
    pass