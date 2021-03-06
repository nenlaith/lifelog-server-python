import connexion

from lifelog.models.read import Read  # noqa: E501


def add_read(body=None):  # noqa: E501
    """Add a new read

     # noqa: E501

    :param body: Read object that needs to be added
    :type body: dict | bytes

    :rtype: Read
    """
    if connexion.request.is_json:
        body = Read.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_read(id):  # noqa: E501
    """delete a specific read

     # noqa: E501

    :param id: id of the specific read
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_read():  # noqa: E501
    """Get all reads

     # noqa: E501


    :rtype: Read
    """
    return 'do some magic!'


def get_read(id):  # noqa: E501
    """get a read with specific id

     # noqa: E501

    :param id: id of the specific read
    :type id: str

    :rtype: Read
    """
    return 'do some magic!'


def update_read(id, body=None):  # noqa: E501
    """update a read at a specific id

     # noqa: E501

    :param id: id of the specific read
    :type id: str
    :param body: Read object that needs to be updated
    :type body: dict | bytes

    :rtype: Read
    """
    if connexion.request.is_json:
        body = Read.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
