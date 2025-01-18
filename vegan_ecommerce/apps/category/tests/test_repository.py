import uuid

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

    def test_get_all_instances_by_CategoryRepository_is_success(self):
        categories = CategoryRepository.get_all_instances()
        self.assertEqual(categories.count(), Category.objects.count())

    def test_get_instance_by_id_by_CategoryRepository_is_success(self):
        category_recovered = CategoryRepository.get_instance_by_id(
            self.category.id)
        self.assertEqual(category_recovered, self.category)

    def test_get_instance_by_id_by_CategoryRepository_raise_CustomApiException_with_NOT_FOUND(self):
        with self.assertRaises(CustomApiException) as cm:
            CategoryRepository.get_instance_by_id(instance_id=uuid.uuid4())
        self.assertEqual(cm.exception.detail, {'error': 'category not found'})
        self.assertEqual(cm.exception.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_instance_by_id_by_CategoryRepository_raise_CustomApiException_with_BAD_REQUEST(self):
        invalid_id = -1
        detail_error_message = f"['“{invalid_id}” is not a valid UUID.']"
        with self.assertRaises(CustomApiException) as cm:
            CategoryRepository.get_instance_by_id(instance_id=invalid_id)
        self.assertEqual(cm.exception.detail, {'error': detail_error_message})
        self.assertEqual(cm.exception.status_code, status.HTTP_400_BAD_REQUEST)
