# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.element import Element  # noqa: F401,E501
from swagger_server import util


class Event(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, element_type: str='event', element_uuid: str=None, element_created_at: datetime=None, element_updated_at: datetime=None, event_timestamp: datetime=None, event_type: str=None):  # noqa: E501
        """Event - a model defined in Swagger

        :param element_type: The element_type of this Event.  # noqa: E501
        :type element_type: str
        :param element_uuid: The element_uuid of this Event.  # noqa: E501
        :type element_uuid: str
        :param element_created_at: The element_created_at of this Event.  # noqa: E501
        :type element_created_at: datetime
        :param element_updated_at: The element_updated_at of this Event.  # noqa: E501
        :type element_updated_at: datetime
        :param event_timestamp: The event_timestamp of this Event.  # noqa: E501
        :type event_timestamp: datetime
        :param event_type: The event_type of this Event.  # noqa: E501
        :type event_type: str
        """
        self.swagger_types = {
            'element_type': str,
            'element_uuid': str,
            'element_created_at': datetime,
            'element_updated_at': datetime,
            'event_timestamp': datetime,
            'event_type': str
        }

        self.attribute_map = {
            'element_type': 'element_type',
            'element_uuid': 'element_uuid',
            'element_created_at': 'element_created_at',
            'element_updated_at': 'element_updated_at',
            'event_timestamp': 'event_timestamp',
            'event_type': 'event_type'
        }
        self._element_type = element_type
        self._element_uuid = element_uuid
        self._element_created_at = element_created_at
        self._element_updated_at = element_updated_at
        self._event_timestamp = event_timestamp
        self._event_type = event_type

    @classmethod
    def from_dict(cls, dikt) -> 'Event':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Event of this Event.  # noqa: E501
        :rtype: Event
        """
        return util.deserialize_model(dikt, cls)

    @property
    def element_type(self) -> str:
        """Gets the element_type of this Event.


        :return: The element_type of this Event.
        :rtype: str
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type: str):
        """Sets the element_type of this Event.


        :param element_type: The element_type of this Event.
        :type element_type: str
        """

        self._element_type = element_type

    @property
    def element_uuid(self) -> str:
        """Gets the element_uuid of this Event.


        :return: The element_uuid of this Event.
        :rtype: str
        """
        return self._element_uuid

    @element_uuid.setter
    def element_uuid(self, element_uuid: str):
        """Sets the element_uuid of this Event.


        :param element_uuid: The element_uuid of this Event.
        :type element_uuid: str
        """

        self._element_uuid = element_uuid

    @property
    def element_created_at(self) -> datetime:
        """Gets the element_created_at of this Event.


        :return: The element_created_at of this Event.
        :rtype: datetime
        """
        return self._element_created_at

    @element_created_at.setter
    def element_created_at(self, element_created_at: datetime):
        """Sets the element_created_at of this Event.


        :param element_created_at: The element_created_at of this Event.
        :type element_created_at: datetime
        """

        self._element_created_at = element_created_at

    @property
    def element_updated_at(self) -> datetime:
        """Gets the element_updated_at of this Event.


        :return: The element_updated_at of this Event.
        :rtype: datetime
        """
        return self._element_updated_at

    @element_updated_at.setter
    def element_updated_at(self, element_updated_at: datetime):
        """Sets the element_updated_at of this Event.


        :param element_updated_at: The element_updated_at of this Event.
        :type element_updated_at: datetime
        """

        self._element_updated_at = element_updated_at

    @property
    def event_timestamp(self) -> datetime:
        """Gets the event_timestamp of this Event.


        :return: The event_timestamp of this Event.
        :rtype: datetime
        """
        return self._event_timestamp

    @event_timestamp.setter
    def event_timestamp(self, event_timestamp: datetime):
        """Sets the event_timestamp of this Event.


        :param event_timestamp: The event_timestamp of this Event.
        :type event_timestamp: datetime
        """
        if event_timestamp is None:
            raise ValueError("Invalid value for `event_timestamp`, must not be `None`")  # noqa: E501

        self._event_timestamp = event_timestamp

    @property
    def event_type(self) -> str:
        """Gets the event_type of this Event.


        :return: The event_type of this Event.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type: str):
        """Sets the event_type of this Event.


        :param event_type: The event_type of this Event.
        :type event_type: str
        """

        self._event_type = event_type