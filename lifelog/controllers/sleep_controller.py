import connexion

from lifelog.models.sleep import Sleep  # noqa: E501


def add_sleep(body=None):  # noqa: E501
    """Add a new sleep

     # noqa: E501

    :param body: Sleep object that needs to be added
    :type body: dict | bytes

    :rtype: Sleep
    """
    if connexion.request.is_json:
        body = Sleep.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_sleep(id):  # noqa: E501
    """delete specific sleep

     # noqa: E501

    :param id: id for the specific sleep
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_sleep():  # noqa: E501
    """Get all sleeps

     # noqa: E501


    :rtype: Sleep
    """
    return 'do some magic!'


def get_sleep(id):  # noqa: E501
    """get a specific sleep

     # noqa: E501

    :param id: id for the specific sleep
    :type id: str

    :rtype: Sleep
    """
    return 'do some magic!'


def update_sleep(id, body=None):  # noqa: E501
    """update a sleep

     # noqa: E501

    :param id: id for the specific sleep
    :type id: str
    :param body: Sleep object that needs to be updated
    :type body: dict | bytes

    :rtype: Sleep
    """
    if connexion.request.is_json:
        body = Sleep.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
