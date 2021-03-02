# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.period import Period  # noqa: F401,E501
from swagger_server import util


class Work(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, element_type: str='period', period_range: str=None, period_type: str='work', period_description: str=''):  # noqa: E501
        """Work - a model defined in Swagger

        :param element_type: The element_type of this Work.  # noqa: E501
        :type element_type: str
        :param period_range: The period_range of this Work.  # noqa: E501
        :type period_range: str
        :param period_type: The period_type of this Work.  # noqa: E501
        :type period_type: str
        :param period_description: The period_description of this Work.  # noqa: E501
        :type period_description: str
        """
        self.swagger_types = {
            'element_type': str,
            'period_range': str,
            'period_type': str,
            'period_description': str
        }

        self.attribute_map = {
            'element_type': 'element_type',
            'period_range': 'period_range',
            'period_type': 'period_type',
            'period_description': 'period_description'
        }
        self._element_type = element_type
        self._period_range = period_range
        self._period_type = period_type
        self._period_description = period_description

    @classmethod
    def from_dict(cls, dikt) -> 'Work':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Work of this Work.  # noqa: E501
        :rtype: Work
        """
        return util.deserialize_model(dikt, cls)

    @property
    def element_type(self) -> str:
        """Gets the element_type of this Work.


        :return: The element_type of this Work.
        :rtype: str
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type: str):
        """Sets the element_type of this Work.


        :param element_type: The element_type of this Work.
        :type element_type: str
        """

        self._element_type = element_type

    @property
    def period_range(self) -> str:
        """Gets the period_range of this Work.


        :return: The period_range of this Work.
        :rtype: str
        """
        return self._period_range

    @period_range.setter
    def period_range(self, period_range: str):
        """Sets the period_range of this Work.


        :param period_range: The period_range of this Work.
        :type period_range: str
        """
        if period_range is None:
            raise ValueError("Invalid value for `period_range`, must not be `None`")  # noqa: E501

        self._period_range = period_range

    @property
    def period_type(self) -> str:
        """Gets the period_type of this Work.


        :return: The period_type of this Work.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type: str):
        """Sets the period_type of this Work.


        :param period_type: The period_type of this Work.
        :type period_type: str
        """

        self._period_type = period_type

    @property
    def period_description(self) -> str:
        """Gets the period_description of this Work.


        :return: The period_description of this Work.
        :rtype: str
        """
        return self._period_description

    @period_description.setter
    def period_description(self, period_description: str):
        """Sets the period_description of this Work.


        :param period_description: The period_description of this Work.
        :type period_description: str
        """

        self._period_description = period_description