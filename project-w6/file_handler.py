import pickle


def read_logs(filename):

    try:

        with open(filename, "r") as file:

            return file.readlines()

    except FileNotFoundError:

        print("Log file not found.")

        return []


def write_invalid_logs(filename, records):

    with open(filename, "w") as file:

        for record in records:

            file.write(record)


def save_valid_records(filename, data):

    with open(filename, "wb") as file:

        pickle.dump(data, file)


def load_valid_records(filename):

    try:

        with open(filename, "rb") as file:

            return pickle.load(file)

    except FileNotFoundError:

        print("Backup file not found.")
        return []