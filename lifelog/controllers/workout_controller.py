import connexion

from lifelog.models.workout import Workout  # noqa: E501


def add_workout(body=None):  # noqa: E501
    """Add a new workout

     # noqa: E501

    :param body: Workout object that needs to be added
    :type body: dict | bytes

    :rtype: Workout
    """
    if connexion.request.is_json:
        body = Workout.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_workout(id):  # noqa: E501
    """delete specified workout

     # noqa: E501

    :param id: id of the workout
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_workout():  # noqa: E501
    """Get all workouts

     # noqa: E501


    :rtype: List[Workout]
    """
    return 'do some magic!'


def get_workout(id):  # noqa: E501
    """get a workout by id

     # noqa: E501

    :param id: id of the workout
    :type id: str

    :rtype: Workout
    """
    return 'do some magic!'


def update_workout(id, body=None):  # noqa: E501
    """update a workout by id

     # noqa: E501

    :param id: id of the workout
    :type id: str
    :param body: Workout object that needs to be updated
    :type body: dict | bytes

    :rtype: Workout
    """
    if connexion.request.is_json:
        body = Workout.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
