# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.work import Work  # noqa: E501
from swagger_server.test import BaseTestCase


class TestWorkController(BaseTestCase):
    """WorkController integration test stubs"""

    def test_add_work(self):
        """Test case for add_work

        Add a new work
        """
        body = Work()
        response = self.client.open(
            '/work',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_work(self):
        """Test case for delete_work

        delete a specific work
        """
        response = self.client.open(
            '/work/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_work(self):
        """Test case for get_all_work

        Get all works
        """
        response = self.client.open(
            '/work',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_work(self):
        """Test case for get_work

        get a work with specific id
        """
        response = self.client.open(
            '/work/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_work(self):
        """Test case for update_work

        update a work at a specific id
        """
        body = Work()
        response = self.client.open(
            '/work/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
