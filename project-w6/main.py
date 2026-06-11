from file_handler import (
    read_logs,
    write_invalid_logs,
    save_valid_records,
    load_valid_records
)

from processor import (
    process_records,
    validate_record
)

from utils.decorator import (
    log_execution
)


@log_execution
def analyze_logs():

    records = read_logs("log.txt")

    valid_records, usernames = (
        process_records(records)
    )

    invalid_records = list(
        filter(
            lambda x:
            not validate_record(x),
            records
        )
    )

    print("\nVALID RECORDS")

    for record in valid_records:

        print(record.strip())

    print("\nUPPERCASE USERNAMES")

    for name in usernames:

        print(name)

    write_invalid_logs(
        "invalid_log.txt",
        invalid_records
    )

    save_valid_records(
        "backup.pkl",
        valid_records
    )

    print("\nDATA FROM PICKLE FILE")

    data = load_valid_records(
        "backup.pkl"
    )

    for record in data:

        print(record.strip())


analyze_logs()