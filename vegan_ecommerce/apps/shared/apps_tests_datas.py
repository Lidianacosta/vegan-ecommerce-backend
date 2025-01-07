from django.template.defaultfilters import slugify


class TestsDatas:

    def get_category_data(self,
                          name='Test category name',
                          description='Test category description',
                          ):
        slug = slugify(name)
        return {
            'name': name,
            'slug': slug,
            'description': description
        }


tests_datas = TestsDatas()
