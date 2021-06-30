from django.urls import path

from .views import images_list, image_create, image_detail


urlpatterns = [
    path("", images_list, name="image_list"),
    path("create/", image_create, name="image_create"),
    path("<int:image_id>/", image_detail, name="image_detail"),
]

