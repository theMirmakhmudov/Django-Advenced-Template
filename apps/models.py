from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}, {self.price}"
