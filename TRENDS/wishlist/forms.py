from django import forms
from ExchangeHub.models import Item

class AddToWishlistForm(forms.Form):
    item_name = forms.CharField(label="Item Name", required=True)
