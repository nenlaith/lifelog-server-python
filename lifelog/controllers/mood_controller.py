import connexion

from lifelog.models.mood import Mood  # noqa: E501


def add_mood(body=None):  # noqa: E501
    """Add a new mood

     # noqa: E501

    :param body: Mood object that needs to be added
    :type body: dict | bytes

    :rtype: Mood
    """
    if connexion.request.is_json:
        body = Mood.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_mood(id):  # noqa: E501
    """delete specified mood

     # noqa: E501

    :param id: id of the mood
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_mood():  # noqa: E501
    """Get all moods

     # noqa: E501


    :rtype: List[Mood]
    """
    return 'do some magic!'


def get_mood(id):  # noqa: E501
    """get a mood by id

     # noqa: E501

    :param id: id of the mood
    :type id: str

    :rtype: Mood
    """
    return 'do some magic!'


def update_mood(id, body=None):  # noqa: E501
    """update a mood by id

     # noqa: E501

    :param id: id of the mood
    :type id: str
    :param body: Mood object that needs to be updated
    :type body: dict | bytes

    :rtype: Mood
    """
    if connexion.request.is_json:
        body = Mood.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
