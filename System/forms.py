from django.forms import ModelForm, extras
from .models import Family, Rent, Car, Grocery


class FamilyForm(ModelForm):

    class Meta:
        model = Family
        fields = ["name"]


class RentForm(ModelForm):

    class Meta:
        model = Rent
        fields = ["family", "title", "value"]


class GroceryForm(ModelForm):
    class Meta:
        model = Grocery
        fields = ["family", "title", "value"]


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["family", "title", "finance", "insurance"]
