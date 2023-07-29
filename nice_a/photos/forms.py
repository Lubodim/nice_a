from django import forms
from django.core.exceptions import ValidationError

from nice_a.common.models import PhotoLike, PhotoComment
from nice_a.core.form_mixin import DisabledFormMixin
from nice_a.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date',)


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'photo')


class PhotoDeleteForm(DisabledFormMixin, PhotoBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.tagged_pets.clear()
            PhotoLike.objects.filter(photo_id=self.instance.id).delete()
            self.instance.delete()
            PhotoComment.objects.filter(photo_id=self.instance.id).delete()

        return self.instance
