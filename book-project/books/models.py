from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year_published = models.PositiveSmallIntegerField()
    publisher_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title
