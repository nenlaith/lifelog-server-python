# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.meal import Meal  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMealController(BaseTestCase):
    """MealController integration test stubs"""

    def test_add_meal(self):
        """Test case for add_meal

        Add a new meal
        """
        body = Meal()
        response = self.client.open(
            '/meal',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_meal(self):
        """Test case for delete_meal

        delete specified meal
        """
        response = self.client.open(
            '/meal/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_meal(self):
        """Test case for get_all_meal

        Get all meals
        """
        response = self.client.open(
            '/meal',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_meal(self):
        """Test case for get_meal

        get a meal by id
        """
        response = self.client.open(
            '/meal/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_meal(self):
        """Test case for update_meal

        update a meal by id
        """
        body = Meal()
        response = self.client.open(
            '/meal/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
