import connexion

from lifelog.models.weigh import Weigh  # noqa: E501


def add_weigh(body=None):  # noqa: E501
    """Add a new weigh

     # noqa: E501

    :param body: Weigh object that needs to be added
    :type body: dict | bytes

    :rtype: Weigh
    """
    if connexion.request.is_json:
        body = Weigh.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_weigh(id):  # noqa: E501
    """delete a weigh with the id specified

     # noqa: E501

    :param id: id of the weigh
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_weigh():  # noqa: E501
    """Get all weighs

     # noqa: E501


    :rtype: Weigh
    """
    return 'do some magic!'


def get_weigh(id):  # noqa: E501
    """get the weigh by id

     # noqa: E501

    :param id: id of the weigh
    :type id: str

    :rtype: Weigh
    """
    return 'do some magic!'


def update_weigh(id, body=None):  # noqa: E501
    """update the weigh the id specified

     # noqa: E501

    :param id: id of the weigh
    :type id: str
    :param body: Weigh object that needs to be updated
    :type body: dict | bytes

    :rtype: Weigh
    """
    if connexion.request.is_json:
        body = Weigh.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
