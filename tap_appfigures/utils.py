"""
Misc. utilities
"""

import copy
from datetime import datetime

from dateutil.parser import parse
from pytz import timezone


def str_to_date(value):
    """
    Convert (json) string to date
    """
    result = parse(value)
    if result.tzinfo is None:
        # All dates (so far) are EST, but this is not part of the data returned by the API
        result = timezone('EST').localize(result)
    return result


def ensure_timezone(value):
    """
    If value (time string) does not have a timezone, add a default tz (EST)

    :param value: string
    :return: string
    """
    return str_to_date(value).strftime("%Y-%m-%d %H:%M:%S%z")


def date_to_str(value):
    """
    Convert date to (json) string
    """
    return value.strftime("%Y-%m-%d %H:%M:%S%z")


class RequestError(Exception):
    """
    Error class for raising an error when a
    request to the AppFigures API fails
    """


def dates_to_str(row_dict):
    """
    Convert all dates to strings - recursively
    """
    result = copy.deepcopy(row_dict)
    for key, value in result.items():
        if isinstance(value, dict):
            result[key] = dates_to_str(value)
        elif isinstance(value, datetime):
            result[key] = date_to_str(value)
    return result
