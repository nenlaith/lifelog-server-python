# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.consumable_mixin import Consumable  # noqa: F401,E501
from swagger_server.models.event import Event  # noqa: F401,E501
from swagger_server import util


class Drink(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, consumable_type: str='liquid', consumable_added_fat: float=0.0, consumable_carbohydrate: float=0.0, consumable_quantity: float=None, element_type: str='event', event_timestamp: datetime=None, event_type: str='drink', drink_category: str=None):  # noqa: E501
        """Drink - a model defined in Swagger

        :param consumable_type: The consumable_type of this Drink.  # noqa: E501
        :type consumable_type: str
        :param consumable_added_fat: The consumable_added_fat of this Drink.  # noqa: E501
        :type consumable_added_fat: float
        :param consumable_carbohydrate: The consumable_carbohydrate of this Drink.  # noqa: E501
        :type consumable_carbohydrate: float
        :param consumable_quantity: The consumable_quantity of this Drink.  # noqa: E501
        :type consumable_quantity: float
        :param element_type: The element_type of this Drink.  # noqa: E501
        :type element_type: str
        :param event_timestamp: The event_timestamp of this Drink.  # noqa: E501
        :type event_timestamp: datetime
        :param event_type: The event_type of this Drink.  # noqa: E501
        :type event_type: str
        :param drink_category: The drink_category of this Drink.  # noqa: E501
        :type drink_category: str
        """
        self.swagger_types = {
            'consumable_type': str,
            'consumable_added_fat': float,
            'consumable_carbohydrate': float,
            'consumable_quantity': float,
            'element_type': str,
            'event_timestamp': datetime,
            'event_type': str,
            'drink_category': str
        }

        self.attribute_map = {
            'consumable_type': 'consumable_type',
            'consumable_added_fat': 'consumable_added_fat',
            'consumable_carbohydrate': 'consumable_carbohydrate',
            'consumable_quantity': 'consumable_quantity',
            'element_type': 'element_type',
            'event_timestamp': 'event_timestamp',
            'event_type': 'event_type',
            'drink_category': 'drink_category'
        }
        self._consumable_type = consumable_type
        self._consumable_added_fat = consumable_added_fat
        self._consumable_carbohydrate = consumable_carbohydrate
        self._consumable_quantity = consumable_quantity
        self._element_type = element_type
        self._event_timestamp = event_timestamp
        self._event_type = event_type
        self._drink_category = drink_category

    @classmethod
    def from_dict(cls, dikt) -> 'Drink':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Drink of this Drink.  # noqa: E501
        :rtype: Drink
        """
        return util.deserialize_model(dikt, cls)

    @property
    def consumable_type(self) -> str:
        """Gets the consumable_type of this Drink.


        :return: The consumable_type of this Drink.
        :rtype: str
        """
        return self._consumable_type

    @consumable_type.setter
    def consumable_type(self, consumable_type: str):
        """Sets the consumable_type of this Drink.


        :param consumable_type: The consumable_type of this Drink.
        :type consumable_type: str
        """

        self._consumable_type = consumable_type

    @property
    def consumable_added_fat(self) -> float:
        """Gets the consumable_added_fat of this Drink.


        :return: The consumable_added_fat of this Drink.
        :rtype: float
        """
        return self._consumable_added_fat

    @consumable_added_fat.setter
    def consumable_added_fat(self, consumable_added_fat: float):
        """Sets the consumable_added_fat of this Drink.


        :param consumable_added_fat: The consumable_added_fat of this Drink.
        :type consumable_added_fat: float
        """
        if consumable_added_fat is None:
            raise ValueError("Invalid value for `consumable_added_fat`, must not be `None`")  # noqa: E501

        self._consumable_added_fat = consumable_added_fat

    @property
    def consumable_carbohydrate(self) -> float:
        """Gets the consumable_carbohydrate of this Drink.

        quantity in [g] for 100g or 100mL  # noqa: E501

        :return: The consumable_carbohydrate of this Drink.
        :rtype: float
        """
        return self._consumable_carbohydrate

    @consumable_carbohydrate.setter
    def consumable_carbohydrate(self, consumable_carbohydrate: float):
        """Sets the consumable_carbohydrate of this Drink.

        quantity in [g] for 100g or 100mL  # noqa: E501

        :param consumable_carbohydrate: The consumable_carbohydrate of this Drink.
        :type consumable_carbohydrate: float
        """
        if consumable_carbohydrate is None:
            raise ValueError("Invalid value for `consumable_carbohydrate`, must not be `None`")  # noqa: E501

        self._consumable_carbohydrate = consumable_carbohydrate

    @property
    def consumable_quantity(self) -> float:
        """Gets the consumable_quantity of this Drink.

        quantity in [g] or [mL]  # noqa: E501

        :return: The consumable_quantity of this Drink.
        :rtype: float
        """
        return self._consumable_quantity

    @consumable_quantity.setter
    def consumable_quantity(self, consumable_quantity: float):
        """Sets the consumable_quantity of this Drink.

        quantity in [g] or [mL]  # noqa: E501

        :param consumable_quantity: The consumable_quantity of this Drink.
        :type consumable_quantity: float
        """

        self._consumable_quantity = consumable_quantity

    @property
    def element_type(self) -> str:
        """Gets the element_type of this Drink.


        :return: The element_type of this Drink.
        :rtype: str
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type: str):
        """Sets the element_type of this Drink.


        :param element_type: The element_type of this Drink.
        :type element_type: str
        """

        self._element_type = element_type

    @property
    def event_timestamp(self) -> datetime:
        """Gets the event_timestamp of this Drink.


        :return: The event_timestamp of this Drink.
        :rtype: datetime
        """
        return self._event_timestamp

    @event_timestamp.setter
    def event_timestamp(self, event_timestamp: datetime):
        """Sets the event_timestamp of this Drink.


        :param event_timestamp: The event_timestamp of this Drink.
        :type event_timestamp: datetime
        """
        if event_timestamp is None:
            raise ValueError("Invalid value for `event_timestamp`, must not be `None`")  # noqa: E501

        self._event_timestamp = event_timestamp

    @property
    def event_type(self) -> str:
        """Gets the event_type of this Drink.


        :return: The event_type of this Drink.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type: str):
        """Sets the event_type of this Drink.


        :param event_type: The event_type of this Drink.
        :type event_type: str
        """

        self._event_type = event_type

    @property
    def drink_category(self) -> str:
        """Gets the drink_category of this Drink.


        :return: The drink_category of this Drink.
        :rtype: str
        """
        return self._drink_category

    @drink_category.setter
    def drink_category(self, drink_category: str):
        """Sets the drink_category of this Drink.


        :param drink_category: The drink_category of this Drink.
        :type drink_category: str
        """
        allowed_values = ["coffee", "tea", "water", "lemon_water"]  # noqa: E501
        if drink_category not in allowed_values:
            raise ValueError(
                "Invalid value for `drink_category` ({0}), must be one of {1}"
                .format(drink_category, allowed_values)
            )

        self._drink_category = drink_category
