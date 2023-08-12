from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    product = models.CharField(max_length=100, default='Unknown Product')
    content = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5),]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.rating not in [1, 2, 3, 4, 5]:
            raise ValidationError({'rating': 'Please select a valid rating between 1 and 5.'})