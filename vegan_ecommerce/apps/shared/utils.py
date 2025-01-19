from django.template.defaultfilters import slugify


class Utils:

    @staticmethod
    def get_slug(base_slug):
        return slugify(base_slug)
