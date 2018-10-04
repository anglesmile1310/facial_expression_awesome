from django import forms

class AbstractForm(forms.Form):
    """
        The abstract form of any request in API views.
        You can extend this form for each use case.
    """
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data