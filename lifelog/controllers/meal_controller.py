import connexion

from lifelog.models.meal import Meal  # noqa: E501


def add_meal(body=None):  # noqa: E501
    """Add a new meal

     # noqa: E501

    :param body: Meal object that needs to be added
    :type body: dict | bytes

    :rtype: Meal
    """
    if connexion.request.is_json:
        body = Meal.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_meal(id):  # noqa: E501
    """delete specified meal

     # noqa: E501

    :param id: id of the meal
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_meal():  # noqa: E501
    """Get all meals

     # noqa: E501


    :rtype: List[Meal]
    """
    return 'do some magic!'


def get_meal(id):  # noqa: E501
    """get a meal by id

     # noqa: E501

    :param id: id of the specific meal
    :type id: str

    :rtype: Meal
    """
    return 'do some magic!'


def update_meal(id, body=None):  # noqa: E501
    """update a meal by id

     # noqa: E501

    :param id: id of the specific meal
    :type id: str
    :param body: Meal object that needs to be updated
    :type body: dict | bytes

    :rtype: Meal
    """
    if connexion.request.is_json:
        body = Meal.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
