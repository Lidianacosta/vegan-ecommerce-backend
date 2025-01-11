from django.template.defaultfilters import slugify

from apps.category.models import Category


class TestsCreateInstanceOfModels:

    def make_category(self,
                      name='category name',
                      description='category description'):

        slug = slugify(name)

        return Category.objects.create(
            name=name,
            slug=slug,
            description=description
        )

    def make_categories(self, count):
        categories = []
        for i in range(count):
            categories.append(self.make_category(
                name=f'category name{i}',
                description=f'category description{i}'
            ))
        return categories


tests_create_instace_of_models = TestsCreateInstanceOfModels()
