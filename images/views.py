from django.shortcuts import get_object_or_404, redirect, render

from .forms import ImageForm, ImageResizeForm
from .models import Image
from .services import image_to_base64, resize_image


def images_list(request):
    images = Image.objects.all()

    ctx = {
        "images": images,
    }
    return render(request, "images/list.html", ctx)


def image_create(request):
    form = ImageForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        image = form.save()
        return redirect("image_detail", image_id=image.id)

    context = {
        "form": form,
    }
    return render(request, "images/create.html", context)


def image_detail(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    base64_image = None

    form = ImageResizeForm(request.POST or None)

    if form.is_valid():
        width = form.cleaned_data.get("width")
        height = form.cleaned_data.get("height")
        resized_image = resize_image(image.source, width=width, height=height)
        base64_image = image_to_base64(resized_image)

    context = {
        "form": form,
        "image": image,
        "base64_image": base64_image,
    }
    return render(request, "images/detail.html", context)
