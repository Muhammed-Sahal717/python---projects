import re


def is_valid_email(email):

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(pattern, email)


def is_valid_time(login_time):

    pattern = r"^([01]\d|2[0-3]):([0-5]\d)$"

    return re.match(pattern, login_time)