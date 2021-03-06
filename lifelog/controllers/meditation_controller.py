import connexion

from lifelog.models.meditation import Meditation  # noqa: E501


def add_meditation(body=None):  # noqa: E501
    """Add a new meditation

     # noqa: E501

    :param body: Meditation object that needs to be added
    :type body: dict | bytes

    :rtype: Meditation
    """
    if connexion.request.is_json:
        body = Meditation.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_meditation(id):  # noqa: E501
    """delete a specific meditation

     # noqa: E501

    :param id: id of the specific meditation
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_meditation():  # noqa: E501
    """Get all meditations

     # noqa: E501


    :rtype: Meditation
    """
    return 'do some magic!'


def get_meditation(id):  # noqa: E501
    """get a meditation with specific id

     # noqa: E501

    :param id: id of the specific meditation
    :type id: str

    :rtype: Meditation
    """
    return 'do some magic!'


def update_meditation(id, body=None):  # noqa: E501
    """update a meditation at a specific id

     # noqa: E501

    :param id: id of the specific meditation
    :type id: str
    :param body: Meditation object that needs to be updated
    :type body: dict | bytes

    :rtype: Meditation
    """
    if connexion.request.is_json:
        body = Meditation.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
