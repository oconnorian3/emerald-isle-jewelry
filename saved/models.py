from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from products.models import Product


class SavedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.slug)])
