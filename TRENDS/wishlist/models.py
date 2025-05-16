from django.db import models
from django.contrib.auth.models import User
from ExchangeHub.models import Item  # Replace 'core' with your app name where Item is defined

class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'session_key', 'item')

    def __str__(self):
        owner = self.user.username if self.user else self.session_key
        return f"{owner} - {self.item.name}"

