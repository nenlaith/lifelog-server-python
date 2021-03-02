# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.watch import Watch  # noqa: E501
from swagger_server.test import BaseTestCase


class TestWatchController(BaseTestCase):
    """WatchController integration test stubs"""

    def test_add_watch(self):
        """Test case for add_watch

        Add a new watch
        """
        body = Watch()
        response = self.client.open(
            '/watch',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_watch(self):
        """Test case for delete_watch

        delete a specific watch
        """
        response = self.client.open(
            '/watch/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_watch(self):
        """Test case for get_all_watch

        Get all watchs
        """
        response = self.client.open(
            '/watch',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_watch(self):
        """Test case for get_watch

        get a watch with specific id
        """
        response = self.client.open(
            '/watch/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_watch(self):
        """Test case for update_watch

        update a watch at a specific id
        """
        body = Watch()
        response = self.client.open(
            '/watch/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
