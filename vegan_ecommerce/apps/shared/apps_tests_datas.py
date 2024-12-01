class TestsDatas:

    def get_category_data(self,
                          name='Test category name',
                          slug='Test category slug',
                          description='Test category description',
                          ):
        return {
            'name': name,
            'slug': slug,
            'description': description
        }


tests_datas = TestsDatas()
