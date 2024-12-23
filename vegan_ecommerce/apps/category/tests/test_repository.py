from django.test import TestCase

from rest_framework import status

from apps.category.models import Category
from apps.category.repository import CategoryRepository
from apps.shared.apps_tests_datas import tests_datas

from apps.shared.custom_api_exception import CustomApiException


class CategoryRepositoryTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            **tests_datas.get_category_data())

    def test_create_instance_by_CategoryRepository_is_success(self):
        category_instance = CategoryRepository.create_instance(
            tests_datas.get_category_data(name='Test create category',
                                          slug='Test create category')
        )
        self.assertIsInstance(category_instance, Category)

    def test_get_all_instances_by_CategoryRepository_is_success(self):
        categories = CategoryRepository.get_all_instances()
        self.assertEqual(categories.count(), Category.objects.count())

    def test_get_instance_by_id_by_CategoryRepository_is_success(self):
        category_recovered = CategoryRepository.get_instance_by_id(
            self.category.id)
        self.assertEqual(category_recovered, self.category)

    def test_update_instance_by_CategoryRepository_is_success(self):
        category_data = tests_datas.get_category_data(
            name='Test update name category',
            slug='Test update slug category',
            description='Test update description'
        )
        category = CategoryRepository.update_instance(
            instance_id=self.category.id, data=category_data)
        self.assertEqual(category.name, category_data['name'])
        self.assertEqual(category.slug, category_data['slug'])
        self.assertEqual(category.description, category_data['description'])

    def test_delete_instance_by_CategoryRepository_is_success(self):
        CategoryRepository.delete_instance(self.category.id)
        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(id=self.category.id)

    def test_get_instance_by_id_by_CategoryRepository_raise_CustomApiException(self):
        with self.assertRaises(CustomApiException) as cm:
            CategoryRepository.get_instance_by_id(instance_id=0)
        self.assertEqual(cm.exception.detail, {'error': 'category not found'})
        self.assertEqual(cm.exception.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_instance_by_CategoryRepository_raise_CustomApiException(self):
        with self.assertRaises(CustomApiException) as cm:
            CategoryRepository.update_instance(instance_id=0, data={})
        self.assertEqual(cm.exception.detail, {'error': 'category not found'})
        self.assertEqual(cm.exception.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_instance_by_CategoryRepository_raise_CustomApiException(self):
        with self.assertRaises(CustomApiException) as cm:
            CategoryRepository.delete_instance(instance_id=0)
        self.assertEqual(cm.exception.detail, {'error': 'category not found'})
        self.assertEqual(cm.exception.status_code, status.HTTP_404_NOT_FOUND)
