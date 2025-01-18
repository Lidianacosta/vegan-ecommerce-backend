import uuid

from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from apps.category.models import Category
from apps.shared.apps_tests_create_instance_of_models import tests_create_instace_of_models
from apps.shared.apps_tests_datas import tests_datas


class CategoryViewSet(APITestCase):
    def setUp(self):
        self.base_url_list_category = "category-list"
        self.base_url_detail_category = "category-detail"
        self.category = tests_create_instace_of_models.make_category()

    def test_list_categories_is_correct_status_code_200_ok(self):
        response = self.client.get(path=reverse(self.base_url_list_category))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_categories_is_sucess(self):
        tests_create_instace_of_models.make_categories(10)
        response = self.client.get(path=reverse(self.base_url_list_category))
        self.assertEqual(len(response.data), Category.objects.count())

    def test_retrieve_category_is_correct_status_code_200_ok(self):
        response = self.client.get(path=reverse(
            self.base_url_detail_category, kwargs={'pk': self.category.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_category_is_invalid_uuid_and_correct_status_code_400_bad_request(self):
        response = self.client.get(path=reverse(
            self.base_url_detail_category, kwargs={'pk': None}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_category_is_correct_status_code_404_not_found(self):
        response = self.client.get(path=reverse(
            self.base_url_detail_category, kwargs={'pk': uuid.uuid4()}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_category_is_success(self):
        response = self.client.get(path=reverse(
            self.base_url_detail_category, kwargs={'pk': self.category.id}))
        self.assertEqual(response.data['id'], str(self.category.id))
        self.assertEqual(response.data['name'], self.category.name)
        self.assertEqual(response.data['slug'], self.category.slug)
        self.assertEqual(response.data['description'],
                         self.category.description)
