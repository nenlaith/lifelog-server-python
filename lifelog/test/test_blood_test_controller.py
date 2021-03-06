# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from lifelog.models.blood_test import BloodTest  # noqa: E501
from lifelog.test import BaseTestCase


class TestBloodTestController(BaseTestCase):
    """BloodTestController integration test stubs"""

    def test_add_blood_test(self):
        """Test case for add_blood_test

        Add a new blood test
        """
        body = BloodTest()
        response = self.client.open(
            '/blood-test',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_blood_test(self):
        """Test case for delete_blood_test

        delete specified blood_test
        """
        response = self.client.open(
            '/blood-test/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_blood_test(self):
        """Test case for get_all_blood_test

        Get all blood tests
        """
        response = self.client.open(
            '/blood-test',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_blood_test(self):
        """Test case for get_blood_test

        get a blood test by id
        """
        response = self.client.open(
            '/blood-test/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_blood_test(self):
        """Test case for update_blood_test

        update a blood test by id
        """
        body = BloodTest()
        response = self.client.open(
            '/blood-test/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
