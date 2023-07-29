# 'ModelForm' and 'Form'
from django import forms

from nice_a.core.form_mixin import DisabledFormMixin
from nice_a.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        # fields =    # '__all__' or (name each field)
        # exclude = ('slug',)  # everything without a slug
        fields = ('name', 'date_of_birth', 'personal_photo')
        labels = {
            'name': 'Pet Name',
            'personal_photo': 'Link to Image',
            'date_of_birth': 'Date of Birth',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Pet name'}
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm-dd-yyyy',
                    'type': 'date'
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={'placeholder': 'Link to image'}
            )
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(DisabledFormMixin, PetBaseForm):
    disabled_fields = ('name', 'date_of_birth', 'personal_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            pass
        return self.instance
