from django import forms
from api.helpers.validators import video_validator
from api.forms.abstract_form import AbstractForm


class VideoExpressionForm(AbstractForm):
    video = forms.FileField(validators=[video_validator])

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
