import json


def read_json(path: str) -> dict:
    """
    A function for reading data from a JSON file and returning a dictionary.

    Parameters
        path: the path to the JSON file to read
    Returns
        Dictionary of data from a JSON file
    """
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"The file '{path}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the JSON file: {str(e)}")


def write_file(path: str, data: list) -> None:
    """
    A function for writing data to a file.

    Parameters
        path: the path to the file to write
        data: data to write to a file
    """
    try:
        with open(path, "w", encoding="UTF-8") as file:
            json.dump({"card_number":  data}, file)
    except FileNotFoundError:
        print(f"The file '{path}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the JSON file: {str(e)}")
