from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Card(models.Model):

    STATUS_KNOW = 1
    STATUS_DONT_KNOW = 2
    STATUS_REPEAT = 3
    STATUS_NEW = 4

    CHOICES_STATUS = [
        (STATUS_KNOW, 'Know'),
        (STATUS_DONT_KNOW, 'Dont know'),
        (STATUS_REPEAT, 'Repeat'),
        (STATUS_NEW, 'New'),
    ]

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="category",
        related_query_name="category"
    )
    name = models.CharField(max_length=200)
    translate = models.CharField(max_length=200)
    image = models.ImageField(upload_to='card/%Y', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=CHOICES_STATUS, default=STATUS_NEW)

    def __str__(self):
        return self.name
