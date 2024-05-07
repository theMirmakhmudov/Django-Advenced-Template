from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}, {self.price}"


class Degree(models.Model):
    Direction_degree = [
        ("JR", "Junior"),
        ("MD", "Middle"),
        ("SN", "Senior"),
        ("SE", "Senior")
    ]

    name = models.CharField(max_length=60)
    degree = models.CharField(max_length=2, choices=Direction_degree)

