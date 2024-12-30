from django.test import TestCase
from apps.category.service import CategoryService
from apps.category.models import Category
from apps.shared.apps_tests_datas import tests_datas
from apps.shared.custom_api_exception import CustomApiException
from rest_framework import status


class CategoryServiceTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            **tests_datas.get_category_data())

    def test_list_all_instances_by_CategoryService_is_success(self):
        categories = CategoryService.list_all_instances()
        self.assertEqual(categories.count(), Category.objects.count())

    def test_create_instance_by_CategoryService_is_success(self):
        category_instance = CategoryService.create_instance(
            **tests_datas.get_category_data(name="Test create category",
                                            slug="Test create category"))

        self.assertIsInstance(category_instance, Category)

    def test_create_instance_by_CategoryService_is_correct_data(self):
        category_name = "Test create category"
        category_slug = "Test create category"
        category = CategoryService.create_instance(
            **tests_datas.get_category_data(name=category_name,
                                            slug=category_slug))

        self.assertEqual(category.name, category_name)
        self.assertEqual(category.slug, category_slug)

    def test_retrieve_instance_by_Category_Service_is_success(self):
        category_recovered = CategoryService.retrieve_instance(
            instance_id=self.category.id)

        self.assertEqual(category_recovered, self.category)

    def test_update_instance_by_CategoryService_is_success(self):
        category_data = tests_datas.get_category_data(
            name='Test upadate name category',
            slug='Test update slug category',
            description='Test update description'
        )
        category = CategoryService.update_instance(
            instance_id=self.category.id, **category_data)
        self.assertEqual(category.name, category_data['name'])
        self.assertEqual(category.slug, category_data['slug'])
        self.assertEqual(category.description, category_data['description'])

    def test_partial_update_instance_name_by_CategoryService_is_success(self):
        category_data = tests_datas.get_category_data(
            name='Test partial upadate name category',
        )
        category = CategoryService.update_instance(
            instance_id=self.category.id, **category_data)
        self.assertEqual(category.name, category_data['name'])

    def test_partial_update_instance_slug_by_CategoryService_is_success(self):
        category_data = tests_datas.get_category_data(
            slug="Test partial update slug category",
        )
        category = CategoryService.update_instance(
            instance_id=self.category.id, **category_data)
        self.assertEqual(category.slug, category_data['slug'])

    def test_partial_update_instance_description_by_CategoryService_is_success(self):
        category_data = tests_datas.get_category_data(
            description='Test partial update description'
        )
        category = CategoryService.update_instance(
            instance_id=self.category.id, **category_data)
        self.assertEqual(category.description, category_data['description'])

    def test_destroy_instance_by_CategoryService_is_success(self):
        CategoryService.destroy_instance(instance_id=self.category.id)
        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(id=self.category.id)

    def test_retrieve_instance_by_id_by_CategoryService_raise_CustomApiException(self):
        with self.assertRaises(CustomApiException) as cm:
            CategoryService.retrieve_instance(instance_id=0)
        self.assertEqual(cm.exception.detail, {'error': 'category not found'})
        self.assertEqual(cm.exception.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_instance_by_id_by_CategoryService_raise_CustomApiException(self):
        with self.assertRaises(CustomApiException) as cm:
            CategoryService.update_instance(instance_id=0)
        self.assertEqual(cm.exception.detail, {'error': 'category not found'})
        self.assertEqual(cm.exception.status_code, status.HTTP_404_NOT_FOUND)

    def test_partial_update_instance_by_id_by_CategoryService_raise_CustomApiException(self):
        with self.assertRaises(CustomApiException) as cm:
            CategoryService.partial_update_instance(instance_id=0)
        self.assertEqual(cm.exception.detail, {'error': 'category not found'})
        self.assertEqual(cm.exception.status_code, status.HTTP_404_NOT_FOUND)

    def test_destroy_instance_by_id_by_CategoryService_raise_CustomApiException(self):
        with self.assertRaises(CustomApiException) as cm:
            CategoryService.destroy_instance(instance_id=0)
        self.assertEqual(cm.exception.detail, {'error': 'category not found'})
        self.assertEqual(cm.exception.status_code, status.HTTP_404_NOT_FOUND)
