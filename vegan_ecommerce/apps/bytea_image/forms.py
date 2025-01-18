from django import forms

from apps.bytea_image.models import ByteaImage
from apps.bytea_image.service import ByteaImageService


class ByteaImageAddForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = ByteaImage
        fields = ('image',)

    def save(self, commit=True):
        image = self.cleaned_data.pop('image')
        obj = super().save(commit=False)
        return ByteaImageService.get_instance_of_bytea_image_from_image(
            image=image, obj=obj, save=commit)


class ByteaImagechangeForm(ByteaImageAddForm):

    class Meta:
        fields = ('image', 'image_name', 'content_type')
