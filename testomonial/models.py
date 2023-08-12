from django.db import models


class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    product = models.CharField(max_length=100, default='Unknown Product')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)