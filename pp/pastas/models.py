from django.db import models

CATEGORIES = [
    ('ns','NSFW'),
    ('ws','Wholesome'),
    ('sb','Sermon'),
    ('bb','Intelligent'),
    ('ha','Funny'),
    ('aw','Sad'),
    ('xx','Flagged')
]

class Pasta(models.Model):
    text = models.TextField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=80, default='', blank=True)
    category = models.CharField(max_length=40, choices=CATEGORIES, default='', blank=True)