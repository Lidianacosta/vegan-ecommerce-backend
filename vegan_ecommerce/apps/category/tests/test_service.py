import uuid

from django.test import TestCase

from rest_framework import status

from apps.category.service import CategoryService
from apps.category.models import Category
from apps.shared.apps_tests_datas import tests_datas
from apps.shared.custom_api_exception import CustomApiException


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
                                            description="Test create category"))

        self.assertIsInstance(category_instance, Category)

    def test_create_instance_by_CategoryService_is_correct_data(self):
        category_name = "Test create category"
        category_description = "Test create category"
        category = CategoryService.create_instance(
            **tests_datas.get_category_data(name=category_name,
                                            description=category_description))

        self.assertEqual(category.name, category_name)
        self.assertEqual(category.description, category_description)

    def test_retrieve_instance_by_Category_Service_is_success(self):
        category_recovered = CategoryService.retrieve_instance(
            instance_id=self.category.id)

        self.assertEqual(category_recovered, self.category)

    def test_update_instance_by_CategoryService_is_success(self):
        category_data = tests_datas.get_category_data(
            name='Test upadate name category',
            description='Test update description'
        )
        category = CategoryService.update_instance(
            instance_id=self.category.id, **category_data)
        self.assertEqual(category.name, category_data['name'])
        self.assertEqual(category.slug, category_data['slug'])
        self.assertEqual(category.description, category_data['description'])

    def test_partial_update_instance_name_by_CategoryService_is_success(self):
        category_data = {}
        category_data['name'] = 'Test partial update description'

        category = CategoryService.partial_update_instance(
            instance_id=self.category.id, **category_data)
        self.assertEqual(category.name, category_data['name'])

    def test_partial_update_instance_slug_by_CategoryService_is_success(self):
        category_data = {}
        category_data['slug'] = 'Test partial update description'

        category = CategoryService.partial_update_instance(
            instance_id=self.category.id, **category_data)
        self.assertEqual(category.slug, category_data['slug'])

    def test_partial_update_instance_description_by_CategoryService_is_success(self):
        category_data = {}
        category_data['description'] = 'Test partial update description'
        category = CategoryService.partial_update_instance(
            instance_id=self.category.id, **category_data)
        self.assertEqual(category.description, category_data['description'])

    def test_destroy_instance_by_CategoryService_is_success(self):
        CategoryService.destroy_instance(instance_id=self.category.id)
        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(id=self.category.id)

    def test_retrieve_instance_by_id_by_CategoryService_raise_CustomApiException_with_not_found(self):
        with self.assertRaises(CustomApiException) as cm:
            CategoryService.retrieve_instance(instance_id=uuid.uuid4())
        self.assertEqual(cm.exception.detail, {'error': 'category not found'})
        self.assertEqual(cm.exception.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_instance_by_id_by_CategoryService_raise_CustomApiException_with_not_found(self):
        category_data = tests_datas.get_category_data()
        with self.assertRaises(CustomApiException) as cm:
            CategoryService.update_instance(
                instance_id=uuid.uuid4(), **category_data)
        self.assertEqual(cm.exception.detail, {'error': 'category not found'})
        self.assertEqual(cm.exception.status_code, status.HTTP_404_NOT_FOUND)

    def test_partial_update_instance_by_id_by_CategoryService_raise_CustomApiException_with_not_found(self):
        with self.assertRaises(CustomApiException) as cm:
            CategoryService.partial_update_instance(instance_id=uuid.uuid4())
        self.assertEqual(cm.exception.detail, {'error': 'category not found'})
        self.assertEqual(cm.exception.status_code, status.HTTP_404_NOT_FOUND)

    def test_destroy_instance_by_id_by_CategoryService_raise_CustomApiException_with_not_found(self):
        with self.assertRaises(CustomApiException) as cm:
            CategoryService.destroy_instance(instance_id=uuid.uuid4())
        self.assertEqual(cm.exception.detail, {'error': 'category not found'})
        self.assertEqual(cm.exception.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_instance_by_id_by_CategoryService_raise_CustomApiException_with_bad_request(self):
        invalid_id = -1
        detail_error_message = f"['“{invalid_id}” is not a valid UUID.']"
        with self.assertRaises(CustomApiException) as cm:
            CategoryService.retrieve_instance(instance_id=invalid_id)
        self.assertEqual(cm.exception.detail, {'error': detail_error_message})
        self.assertEqual(cm.exception.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_instance_by_id_by_CategoryService_raise_CustomApiException_with_bad_request(self):
        invalid_id = -1
        detail_error_message = f"['“{invalid_id}” is not a valid UUID.']"
        category_data = tests_datas.get_category_data()
        with self.assertRaises(CustomApiException) as cm:
            CategoryService.update_instance(
                instance_id=invalid_id, **category_data)
        self.assertEqual(cm.exception.detail, {'error': detail_error_message})
        self.assertEqual(cm.exception.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_instance_by_id_by_CategoryService_raise_CustomApiException_with_bad_request(self):
        invalid_id = -1
        detail_error_message = f"['“{invalid_id}” is not a valid UUID.']"
        with self.assertRaises(CustomApiException) as cm:
            CategoryService.partial_update_instance(instance_id=invalid_id)
        self.assertEqual(cm.exception.detail, {'error': detail_error_message})
        self.assertEqual(cm.exception.status_code, status.HTTP_400_BAD_REQUEST)

    def test_destroy_instance_by_id_by_CategoryService_raise_CustomApiException_with_bad_request(self):
        invalid_id = -1
        detail_error_message = f"['“{invalid_id}” is not a valid UUID.']"
        with self.assertRaises(CustomApiException) as cm:
            CategoryService.destroy_instance(instance_id=invalid_id)
        self.assertEqual(cm.exception.detail, {'error': detail_error_message})
        self.assertEqual(cm.exception.status_code, status.HTTP_400_BAD_REQUEST)
