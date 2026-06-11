from validator import (
    is_valid_email,
    is_valid_time
)


def validate_record(line):

    parts = line.strip().split()

    if len(parts) != 3:
        return False

    username, email, login_time = parts

    return (
        is_valid_email(email)
        and
        is_valid_time(login_time)
    )


def process_records(records):

    valid_records = list(
        filter(
            validate_record,
            records
        )
    )

    usernames = list(
        map(
            lambda x: x.split()[0].upper(),
            valid_records
        )
    )

    return valid_records, usernames