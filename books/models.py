from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False)
    published_date = models.DateField(null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0.0)
    genre = models.CharField(max_length=100, blank=True)
    isbn = models.CharField(max_length=13, unique=True, null=False)

    def __str__(self):
        return self.title
