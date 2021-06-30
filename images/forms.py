from django import forms
from django.core import files

from .models import Image
from .services import get_image_from_url


class ImageForm(forms.ModelForm):
    image_url = forms.URLField(label="Ссылка", required=False)
    source = forms.ImageField(label="Файл", required=False)

    class Meta:
        model = Image
        fields = [
            "image_url",
            "source",
        ]

    def clean(self):
        cleaned_data = super().clean()
        image_url = cleaned_data.get("image_url")
        source = cleaned_data.get("source")

        if image_url and source:
            raise forms.ValidationError("Отправьте либо ссылку, либо изображение.")

        if image_url:
            image, name = get_image_from_url(image_url)

            if image is None:
                raise forms.ValidationError("Не удалось загрузить изображение по ссылке.")
            
            source = files.File(image, name=name)

        cleaned_data["source"] = source

        return cleaned_data


class ImageResizeForm(forms.Form):
    width = forms.IntegerField(label="Ширина", min_value=1, required=False)
    height = forms.IntegerField(label="Высота", min_value=1, required=False)

    def clean(self):
        cleaned_data = super().clean()
        width = cleaned_data.get("width")
        height = cleaned_data.get("height")

        if width is None and height is None:
            raise forms.ValidationError("Выберите либо высоту, либо ширину картинки.")

        return cleaned_data
