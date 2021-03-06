# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from lifelog.models.sleep import Sleep  # noqa: E501
from lifelog.test import BaseTestCase


class TestSleepController(BaseTestCase):
    """SleepController integration test stubs"""

    def test_add_sleep(self):
        """Test case for add_sleep

        Add a new sleep
        """
        body = Sleep()
        response = self.client.open(
            '/sleep',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_sleep(self):
        """Test case for delete_sleep

        delete specific sleep
        """
        response = self.client.open(
            '/sleep/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_sleep(self):
        """Test case for get_all_sleep

        Get all sleeps
        """
        response = self.client.open(
            '/sleep',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_sleep(self):
        """Test case for get_sleep

        get a specific sleep
        """
        response = self.client.open(
            '/sleep/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_sleep(self):
        """Test case for update_sleep

        update a sleep
        """
        body = Sleep()
        response = self.client.open(
            '/sleep/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
