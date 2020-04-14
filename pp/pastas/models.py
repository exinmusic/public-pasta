from django.db import models

CATEGORIES = [
    ('wholesome','wholesome'),
    ('sermon','sermon'),
    ('intelligent','intelligent'),
    ('funny','funny'),
    ('sad','sad'),
    ('politics','politics'),
    ('complaint','complaint'),
    ('emojis','emojis'),
    ('flagged','flagged')
]

class Pasta(models.Model):
    text = models.TextField(max_length=15000)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=500, default='', blank=True)
    category = models.CharField(max_length=40, choices=CATEGORIES, default='', blank=True)