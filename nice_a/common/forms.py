from django import forms

from nice_a.common.models import PhotoComment


class PhotoCommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cows': 40,
                    'rows': 10,
                    'placeholder': "Add Comment...",
                }
            )
        }


class PhotoSearchForm(forms.Form):
    pet_name = forms.CharField(
        max_length=50,
        required=False,
    )
