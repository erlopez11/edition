from django.forms import ModelForm
from cloudinary.forms import CloudinaryFileField
from .models import Edition

class EditionForm(ModelForm):
    image = CloudinaryFileField()
    class Meta:
        model = Edition
        fields = ['edition_name', 'image', 'year', 'edition_size', 'paper_size', 'plate_size', 'technique', 'margin_upper', 'margin_lower', 'margin_sides', 'available_prints', 'status', 'edition_type']