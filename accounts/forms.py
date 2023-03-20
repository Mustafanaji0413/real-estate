from django.forms import ModelForm
from listings.models import Listing


class listingForm(ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
