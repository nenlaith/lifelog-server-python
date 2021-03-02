import connexion
import six

from swagger_server.models.span import Span  # noqa: E501
from swagger_server import util


def get_day_by_date(_date):  # noqa: E501
    """get all informations for a specific date

     # noqa: E501

    :param _date: date interested in
    :type _date: str

    :rtype: Span
    """
    _date = util.deserialize_date(_date)
    return 'do some magic!'


def get_day_by_number(number):  # noqa: E501
    """get informations about a day before today

     # noqa: E501

    :param number: {number} of days before today. if {number} &#x3D; 0 it is equivalent to /today
    :type number: int

    :rtype: Span
    """
    return 'do some magic!'


def get_month_by_name(name):  # noqa: E501
    """get all the informations about a month by name

     # noqa: E501

    :param name: the name must be in english: january, february etc... in short or long version (i.e. january or jan )
    :type name: str

    :rtype: List[Span]
    """
    return 'do some magic!'


def get_month_by_number(number):  # noqa: E501
    """get all the informations about a month before this one

     # noqa: E501

    :param number: if {number} &#x3D; 0 it is equivalent to /tomonth. {number} &lt; 0 &#x3D;&gt; {number} months before this one.
    :type number: int

    :rtype: List[Span]
    """
    return 'do some magic!'


def get_to_day():  # noqa: E501
    """get all informations for today

     # noqa: E501


    :rtype: Span
    """
    return 'do some magic!'


def get_to_month():  # noqa: E501
    """get all informations for this month

     # noqa: E501


    :rtype: List[Span]
    """
    return 'do some magic!'


def get_to_week():  # noqa: E501
    """get all informations for this week

     # noqa: E501


    :rtype: List[Span]
    """
    return 'do some magic!'


def get_to_year():  # noqa: E501
    """get all informations for this year

     # noqa: E501


    :rtype: List[Span]
    """
    return 'do some magic!'


def get_week(number):  # noqa: E501
    """get all informations for the week {number} before

     # noqa: E501

    :param number: - {number} &#x3D; 0 &#x3D;&gt; return the current week. equivalent /toweek - {number} &lt; 0 &#x3D;&gt; {number} represent how many week   before the current one.
    :type number: int

    :rtype: Span
    """
    return 'do some magic!'


def get_year_by_number(year):  # noqa: E501
    """get all the informations about a year by number

     # noqa: E501

    :param year: {number} &#x3D; 19xx or 20xx
    :type year: int

    :rtype: List[Span]
    """
    return 'do some magic!'
