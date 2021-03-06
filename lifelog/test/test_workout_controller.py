# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from lifelog.models.workout import Workout  # noqa: E501
from lifelog.test import BaseTestCase


class TestWorkoutController(BaseTestCase):
    """WorkoutController integration test stubs"""

    def test_add_workout(self):
        """Test case for add_workout

        Add a new workout
        """
        body = Workout()
        response = self.client.open(
            '/workout',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_workout(self):
        """Test case for delete_workout

        delete specified workout
        """
        response = self.client.open(
            '/workout/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_workout(self):
        """Test case for get_all_workout

        Get all workouts
        """
        response = self.client.open(
            '/workout',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_workout(self):
        """Test case for get_workout

        get a workout by id
        """
        response = self.client.open(
            '/workout/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_workout(self):
        """Test case for update_workout

        update a workout by id
        """
        body = Workout()
        response = self.client.open(
            '/workout/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
