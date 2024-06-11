from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^1\d{10}$',
    message="Phone number must be 10 digits long and start with '1'."
)

class Order(models.Model):
    """
    Order Model
    Defines the attributes of a order
    """


    title = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0"))]
    )
    poster_phone_number = models.CharField(
        validators=[phone_regex], max_length=11
    )
    is_accepted = models.BooleanField(default=False)
    is_digital = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

