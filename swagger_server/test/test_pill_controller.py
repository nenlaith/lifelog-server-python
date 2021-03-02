# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.pill import Pill  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPillController(BaseTestCase):
    """PillController integration test stubs"""

    def test_add_pill(self):
        """Test case for add_pill

        Add a new pill
        """
        body = Pill()
        response = self.client.open(
            '/pill',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_pill(self):
        """Test case for delete_pill

        delete specified pill
        """
        response = self.client.open(
            '/pill/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_pill(self):
        """Test case for get_all_pill

        Get all pills
        """
        response = self.client.open(
            '/pill',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_pill(self):
        """Test case for get_pill

        get a pill by id
        """
        response = self.client.open(
            '/pill/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_pill(self):
        """Test case for update_pill

        update a pill by id
        """
        body = Pill()
        response = self.client.open(
            '/pill/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
