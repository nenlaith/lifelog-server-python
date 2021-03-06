import connexion

from lifelog.models.work import Work  # noqa: E501


def add_work(body=None):  # noqa: E501
    """Add a new work

     # noqa: E501

    :param body: Work object that needs to be added
    :type body: dict | bytes

    :rtype: Work
    """
    if connexion.request.is_json:
        body = Work.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_work(id):  # noqa: E501
    """delete a specific work

     # noqa: E501

    :param id: id of the specific work
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_work():  # noqa: E501
    """Get all works

     # noqa: E501


    :rtype: Work
    """
    return 'do some magic!'


def get_work(id):  # noqa: E501
    """get a work with specific id

     # noqa: E501

    :param id: id of the specific work
    :type id: str

    :rtype: Work
    """
    return 'do some magic!'


def update_work(id, body=None):  # noqa: E501
    """update a work at a specific id

     # noqa: E501

    :param id: id of the specific work
    :type id: str
    :param body: Work object that needs to be updated
    :type body: dict | bytes

    :rtype: Work
    """
    if connexion.request.is_json:
        body = Work.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
