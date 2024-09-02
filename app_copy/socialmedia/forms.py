from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Publications
from django.forms import BaseInlineFormSet


class SocialForm(ModelForm):

    class Meta:
        model = Publications
        fields = ["title", "description", "image"]

    def clean(self):
        cleaned_data = super().clean()
        delete_image = cleaned_data.get('delete_image')
        if delete_image and not cleaned_data.get('image'):
            raise forms.ValidationError('You cannot delete the image if no image is provided.')
        return cleaned_data
