# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.weigh import Weigh  # noqa: E501
from swagger_server.test import BaseTestCase


class TestWeighController(BaseTestCase):
    """WeighController integration test stubs"""

    def test_add_weigh(self):
        """Test case for add_weigh

        Add a new weigh
        """
        body = Weigh()
        response = self.client.open(
            '/weigh',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_weigh(self):
        """Test case for delete_weigh

        delete a weigh with the id specified
        """
        response = self.client.open(
            '/weigh/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_weigh(self):
        """Test case for get_all_weigh

        Get all weighs
        """
        response = self.client.open(
            '/weigh',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_weigh(self):
        """Test case for get_weigh

        get the weigh by id
        """
        response = self.client.open(
            '/weigh/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_weigh(self):
        """Test case for update_weigh

        update the weigh the id specified
        """
        body = Weigh()
        response = self.client.open(
            '/weigh/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
