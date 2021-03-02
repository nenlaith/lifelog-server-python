import connexion
import six

from swagger_server.models.watch import Watch  # noqa: E501
from swagger_server import util


def add_watch(body=None):  # noqa: E501
    """Add a new watch

     # noqa: E501

    :param body: Watch object that needs to be added
    :type body: dict | bytes

    :rtype: Watch
    """
    if connexion.request.is_json:
        body = Watch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_watch(id):  # noqa: E501
    """delete a specific watch

     # noqa: E501

    :param id: id of the specific watch
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_watch():  # noqa: E501
    """Get all watchs

     # noqa: E501


    :rtype: Watch
    """
    return 'do some magic!'


def get_watch(id):  # noqa: E501
    """get a watch with specific id

     # noqa: E501

    :param id: id of the specific watch
    :type id: str

    :rtype: Watch
    """
    return 'do some magic!'


def update_watch(id, body=None):  # noqa: E501
    """update a watch at a specific id

     # noqa: E501

    :param id: id of the specific watch
    :type id: str
    :param body: Watch object that needs to be updated
    :type body: dict | bytes

    :rtype: Watch
    """
    if connexion.request.is_json:
        body = Watch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
