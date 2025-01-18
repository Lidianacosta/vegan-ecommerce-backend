from django.http import HttpResponse
from apps.bytea_image.service import ByteaImageService


def get_image(request, uuid):
    bytea_image = ByteaImageService.get_instance_by_id_or_404(uuid)

    return HttpResponse(
        bytea_image.image_data,
        content_type=bytea_image.content_type
    )
