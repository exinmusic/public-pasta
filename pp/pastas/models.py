from django.db import models
from multiselectfield import MultiSelectField

# Categor
CATEGORIES = [
    ('wholesome','wholesome'),      # Feel good content or good natured.
    ('sermon','sermon'),            # Preaching. Written with arrogance.
    ('intelligent','intelligent'),  # Not ironically intelligent, as much as possible.
    ('dumb','dumb'),                # Just really unredeemingly stupid.
    ('funny','funny'),              # is funny.
    ('sad','sad'),                  # is sad.
    ('political','political'),      # Flags anything political, includes mentions of politicians.
    ('complaint','complaint'),      # Flags compaints.
    ('emoji','emoji'),              # Content with exessive use of emoticons.
    ('daddy','daddy'),              # Content written "to" sugar daddies.
    ('sexy','sexy'),                # Sexual Content.
    ('pro','pro'),                  # Professional advise.
    ('creepy', 'creepy'),           # Creepy or dark in nature.
    ('food', 'food'),               # Food
    ('nsfw','nsfw')                 # Content with this flag will not appear in clean search results.
]

SENTIMENTS = [
    ('positive', 'positive'),
    ('negative', 'negative')
]


class Pasta(models.Model):
    text         = models.TextField(max_length=15000)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    name         = models.CharField(max_length=500, default='', blank=True)
    categories   = MultiSelectField(max_length=150, choices=CATEGORIES, default='', blank=True)
    long         = models.BooleanField(default=False)
    sentiment    = models.CharField(max_length=8, choices=SENTIMENTS, default='', blank=True)
    def __str__(self):
        return self.name
    