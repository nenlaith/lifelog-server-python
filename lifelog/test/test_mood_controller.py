# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from lifelog.models.mood import Mood  # noqa: E501
from lifelog.test import BaseTestCase


class TestMoodController(BaseTestCase):
    """MoodController integration test stubs"""

    def test_add_mood(self):
        """Test case for add_mood

        Add a new mood
        """
        body = Mood()
        response = self.client.open(
            '/mood',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_mood(self):
        """Test case for delete_mood

        delete specified mood
        """
        response = self.client.open(
            '/mood/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_mood(self):
        """Test case for get_all_mood

        Get all moods
        """
        response = self.client.open(
            '/mood',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mood(self):
        """Test case for get_mood

        get a mood by id
        """
        response = self.client.open(
            '/mood/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_mood(self):
        """Test case for update_mood

        update a mood by id
        """
        body = Mood()
        response = self.client.open(
            '/mood/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
