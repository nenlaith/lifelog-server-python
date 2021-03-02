import connexion
import six

from swagger_server.models.drink import Drink  # noqa: E501
from swagger_server import util


def add_drink(body=None):  # noqa: E501
    """Add a new drink

     # noqa: E501

    :param body: Drink object that needs to be added
    :type body: dict | bytes

    :rtype: Drink
    """
    if connexion.request.is_json:
        body = Drink.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_drink(id):  # noqa: E501
    """delete specified drink

     # noqa: E501

    :param id: id of the drink
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_drink():  # noqa: E501
    """Get all drinks

     # noqa: E501


    :rtype: Drink
    """
    return 'do some magic!'


def get_drink(id):  # noqa: E501
    """get a drink by id

     # noqa: E501

    :param id: id of the drink
    :type id: str

    :rtype: Drink
    """
    return 'do some magic!'


def update_drink(id, body=None):  # noqa: E501
    """update a drink

     # noqa: E501

    :param id: id of the drink
    :type id: str
    :param body: Drink object that needs to be updated
    :type body: dict | bytes

    :rtype: Drink
    """
    if connexion.request.is_json:
        body = Drink.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
