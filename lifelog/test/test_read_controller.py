# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from lifelog.models.read import Read  # noqa: E501
from lifelog.test import BaseTestCase


class TestReadController(BaseTestCase):
    """ReadController integration test stubs"""

    def test_add_read(self):
        """Test case for add_read

        Add a new read
        """
        body = Read()
        response = self.client.open(
            '/read',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_read(self):
        """Test case for delete_read

        delete a specific read
        """
        response = self.client.open(
            '/read/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_read(self):
        """Test case for get_all_read

        Get all reads
        """
        response = self.client.open(
            '/read',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_read(self):
        """Test case for get_read

        get a read with specific id
        """
        response = self.client.open(
            '/read/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_read(self):
        """Test case for update_read

        update a read at a specific id
        """
        body = Read()
        response = self.client.open(
            '/read/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
