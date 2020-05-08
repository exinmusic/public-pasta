from django.db import models

CATEGORIES = [
    ('wholesome','wholesome'),      # Feel good content or good natured.
    ('sermon','sermon'),            # Preaching. Written with arrogance.
    ('intelligent','intelligent'),  # Not ironically intelligent, as much as possible.
    ('funny','funny'),              # Sentiment is mostly funny.
    ('sad','sad'),                  # Sentiment is mostly sad.
    ('political','political'),      # Flags anything political, includes mentions of politicians.
    ('complaint','complaint'),      # Flags compaints.
    ('emoji','emoji'),              # Content with exessive use of emoticons.
    ('daddy','daddy'),              # Content written "to" sugar daddies.
    ('sexy','sexy')                 # Sexual Content.
    ('pro','pro'),                  # Professional advise.
    ('nsfw','nsfw')                 # Content with this flag will not appear in clean search results.
]

class Pasta(models.Model):
    text = models.TextField(max_length=15000)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=500, default='', blank=True)
    category = models.CharField(max_length=40, choices=CATEGORIES, default='', blank=True)