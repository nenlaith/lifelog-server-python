# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from lifelog.models.drink import Drink  # noqa: E501
from lifelog.test import BaseTestCase


class TestDrinkController(BaseTestCase):
    """DrinkController integration test stubs"""

    def test_add_drink(self):
        """Test case for add_drink

        Add a new drink
        """
        body = Drink()
        response = self.client.open(
            '/drink',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_drink(self):
        """Test case for delete_drink

        delete specified drink
        """
        response = self.client.open(
            '/drink/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_drink(self):
        """Test case for get_all_drink

        Get all drinks
        """
        response = self.client.open(
            '/drink',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_drink(self):
        """Test case for get_drink

        get a drink by id
        """
        response = self.client.open(
            '/drink/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_drink(self):
        """Test case for update_drink

        update a drink
        """
        body = Drink()
        response = self.client.open(
            '/drink/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
