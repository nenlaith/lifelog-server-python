# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from lifelog.models.span import Span  # noqa: E501
from lifelog.test import BaseTestCase


class TestSpanController(BaseTestCase):
    """SpanController integration test stubs"""

    def test_get_day_by_date(self):
        """Test case for get_day_by_date

        get all informations for a specific date
        """
        response = self.client.open(
            '/day/{date}'.format(_date='2013-10-20'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_day_by_number(self):
        """Test case for get_day_by_number

        get informations about a day before today
        """
        response = self.client.open(
            '/day/{number}'.format(number=0),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_month_by_name(self):
        """Test case for get_month_by_name

        get all the informations about a month by name
        """
        response = self.client.open(
            '/month/{name}'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_month_by_number(self):
        """Test case for get_month_by_number

        get all the informations about a month before this one
        """
        response = self.client.open(
            '/month/{number}'.format(number=0),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_to_day(self):
        """Test case for get_to_day

        get all informations for today
        """
        response = self.client.open(
            '/today',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_to_month(self):
        """Test case for get_to_month

        get all informations for this month
        """
        response = self.client.open(
            '/tomonth',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_to_week(self):
        """Test case for get_to_week

        get all informations for this week
        """
        response = self.client.open(
            '/toweek',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_to_year(self):
        """Test case for get_to_year

        get all informations for this year
        """
        response = self.client.open(
            '/toyear',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_week(self):
        """Test case for get_week

        get all informations for the week {number} before
        """
        response = self.client.open(
            '/week/{number}'.format(number=0),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_year_by_number(self):
        """Test case for get_year_by_number

        get all the informations about a year by number
        """
        response = self.client.open(
            '/year/{year}'.format(year=1971),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
