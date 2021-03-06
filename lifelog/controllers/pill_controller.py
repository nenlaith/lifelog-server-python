import connexion

from lifelog.models.pill import Pill  # noqa: E501


def add_pill(body=None):  # noqa: E501
    """Add a new pill

     # noqa: E501

    :param body: Pill object that needs to be added
    :type body: dict | bytes

    :rtype: Pill
    """
    if connexion.request.is_json:
        body = Pill.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_pill(id):  # noqa: E501
    """delete specified pill

     # noqa: E501

    :param id: id of the pill
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_pill():  # noqa: E501
    """Get all pills

     # noqa: E501


    :rtype: Pill
    """
    return 'do some magic!'


def get_pill(id):  # noqa: E501
    """get a pill by id

     # noqa: E501

    :param id: id of the pill
    :type id: str

    :rtype: Pill
    """
    return 'do some magic!'


def update_pill(id, body=None):  # noqa: E501
    """update a pill by id

     # noqa: E501

    :param id: id of the pill
    :type id: str
    :param body: Pill object that needs to be updated
    :type body: dict | bytes

    :rtype: Pill
    """
    if connexion.request.is_json:
        body = Pill.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
