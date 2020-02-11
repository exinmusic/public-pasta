from django.db import models

CATEGORIES = [
    ('ns','NSFW'),
    ()
]

class Pasta(models.Model):
    text = models.TextField(max_length=600)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=80, default='', blank=True)
    category = models.
