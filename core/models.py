from django.db import models
from django.conf import settings

CATEGORY_CHOICES = (
    ('PER', 'Percusión'),
    ('CUE', 'Cuerda'),
    ('VIE', 'Viento')
)


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.IntegerField(max_length=9, default=0)
    #category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)

    def __str__(self) -> str:
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateField(auto_now_add=True)
    ordered_date = models.DateField()
    ordered = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username
