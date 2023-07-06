from django.db import models

class Article(models.Model):
    id = models.IntegerField()
    title = models.TextField()
    content = models.TextField()
