import connexion

from lifelog.models.blood_test import BloodTest  # noqa: E501


def add_blood_test(body=None):  # noqa: E501
    """Add a new blood test

     # noqa: E501

    :param body: BloodTest object that needs to be added
    :type body: dict | bytes

    :rtype: BloodTest
    """
    if connexion.request.is_json:
        body = BloodTest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_blood_test(id):  # noqa: E501
    """delete specified blood_test

     # noqa: E501

    :param id: id of the blood test
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_blood_test():  # noqa: E501
    """Get all blood tests

     # noqa: E501


    :rtype: List[BloodTest]
    """
    return 'do some magic!'


def get_blood_test(id):  # noqa: E501
    """get a blood test by id

     # noqa: E501

    :param id: id of the blood test
    :type id: str

    :rtype: BloodTest
    """
    return 'do some magic!'


def update_blood_test(id, body=None):  # noqa: E501
    """update a blood test by id

     # noqa: E501

    :param id: id of the blood test
    :type id: str
    :param body: BloodTest object that needs to be updated
    :type body: dict | bytes

    :rtype: BloodTest
    """
    if connexion.request.is_json:
        body = BloodTest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
