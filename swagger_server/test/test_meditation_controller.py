# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.meditation import Meditation  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMeditationController(BaseTestCase):
    """MeditationController integration test stubs"""

    def test_add_meditation(self):
        """Test case for add_meditation

        Add a new meditation
        """
        body = Meditation()
        response = self.client.open(
            '/meditation',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_meditation(self):
        """Test case for delete_meditation

        delete a specific meditation
        """
        response = self.client.open(
            '/meditation/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_meditation(self):
        """Test case for get_all_meditation

        Get all meditations
        """
        response = self.client.open(
            '/meditation',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_meditation(self):
        """Test case for get_meditation

        get a meditation with specific id
        """
        response = self.client.open(
            '/meditation/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_meditation(self):
        """Test case for update_meditation

        update a meditation at a specific id
        """
        body = Meditation()
        response = self.client.open(
            '/meditation/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
