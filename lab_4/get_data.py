import csv
import datetime
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)


def get_data_from_x_y(file_name_x: str, file_name_y: str, date: datetime.date) -> list[str] or None:
    """Function finds information about date from X.csv and Y.csv files

    Args:
        file_name_x (str): Path to file that contains dates
        file_name_y (str): Path to file that contains data
        date (datetime.date): The date for which you want to find weather data

    Raises:
        FileNotFoundError: One or both of the files are missing

    Returns:
        list[str] or None: returns list[str] if data for the date was found, or returns None on failure
    """

    if os.path.exists(file_name_x) and os.path.exists(file_name_y):
        logging.info(f"Files found: {file_name_x}, {file_name_y}")
        with open(file_name_x, "r", encoding="utf-8") as x:
            dates = list(csv.reader(x, delimiter=","))
            index = -1
            for i in range(len(dates)):
                if dates[i][0] == str(date):
                    index = i
                    break
        with open(file_name_y, "r", encoding="utf-8") as y:
            data = list(csv.reader(y, delimiter=","))
            if index >= 0:
                logging.info(f"Data found for date {date}: {data[index]}")
                return data[index]
            elif index == -1:
                logging.warning(f"No data found for date {date}")
                return None
    logging.error("FileNotFoundError: One or both of the files are missing.")
    raise FileNotFoundError


def get_data_from_years_and_weeks(folder_name: str, date: datetime.date) -> list[str] or None:
    """Function finds information about date from csv files that contains data

    Args:
        folder_name (str): Path to folder that contains .csv files
        date (datetime.date): The date for which you want to find weather data

    Raises:
        FileNotFoundError: Folder with .csv files is missing

    Returns:
        list[str] or None: list[str] or None: returns list[str] if data for the
        date was found, or returns None on failure
    """
    if os.path.exists(folder_name):
        logging.info(f"Folder found: {folder_name}")
        index = -1
        for root, dirs, files in os.walk(folder_name):
            for file in files:
                with open(os.path.join(folder_name, file), "r", encoding="utf-8") as csv_file:
                    dates = list(csv.reader(csv_file, delimiter=","))
                    for i in range(len(dates)):
                        if dates[i][0] == str(date):
                            index = i
                            break
                    if index >= 0:
                        logging.info(f"Data found for date {date} in file {file}: {dates[i][1:]}")
                        return dates[i][1:]
        if index == -1:
            logging.warning(f"No data found for date {date} in folder {folder_name}")
            return None
        else:
            logging.error("FileNotFoundError: Folder with .csv files is missing")
            raise FileNotFoundError


def get_data(file_name: str, date: datetime.date) -> list[str] or None:
    """Function finds information about date from csv file
    Args:
        file_name (str): Path to file that contains weather data about dates
        date (datetime.date): The date for which you want to find weather data

    Raises:
        FileNotFoundError: .csv file is missing

    Returns:
        list[str] or None: list[str] or None: returns list[str] if data for the
        date was found, or returns None on failure
    """
    if os.path.exists(file_name):
        logging.info(f"File found: {file_name}")
        with open(file_name, "r", encoding="utf-8") as csv_file:
            reader_object = list(csv.reader(csv_file, delimiter=","))
            for i in range(len(reader_object)):
                if reader_object[i][0] == str(date):
                    logging.info(f"Data found for date {date}: {reader_object[i][1:]}")
                    return reader_object[i][1:]
    else:
        logging.error("FileNotFoundError: .csv file is missing")
        raise FileNotFoundError


class DateIterator:
    """Class for iterating over data in a CSV file."""
    def __init__(self):
        """Initialize the DateIterator."""
        self.counter = 0
        self.file_name = "result.csv"

    def __next__(self) -> tuple:
        """Get the next tuple of data from the CSV file.

        Returns:
            tuple: A tuple of data from the CSV file.

        Raises:
            StopIteration: When the end of the file is reached.
            FileNotFoundError: If the file does not exist.
        """
        if os.path.exists(self.file_name):
            logging.info(f"Opening file for iteration: {self.file_name}")
            with open(self.file_name, "r", encoding="utf-8") as csv_file:
                reader_object = list(csv.reader(csv_file, delimiter=","))
                if self.counter == len(reader_object):
                    logging.info("End of file reached.")
                    raise StopIteration
                elif self.counter < len(reader_object):
                    self.counter += 1
                    output = (
                        reader_object[self.counter - 1][0],
                        reader_object[self.counter - 1][1],
                        reader_object[self.counter - 1][2],
                        reader_object[self.counter - 1][3],
                        reader_object[self.counter - 1][4],
                        reader_object[self.counter - 1][5],
                        reader_object[self.counter - 1][6]
                    )
                    return output
        else:
            logging.error("FileNotFoundError: File does not exist.")
            raise FileNotFoundError


if __name__ == "__main__":
    try:
        file_name = "result.csv"
        folder_name_years = "data_to_years_output"
        folder_name_weeks = "data_to_weeks_output"
        file_name_x = "divide_data_output//X.csv"
        file_name_y = "divide_data_output//Y.csv"

        date = datetime.date(2010, 1, 5)
        invalid_date = datetime.date(2222, 5, 20)
        obj = DateIterator()
    except FileNotFoundError:
        logging.error("No such file exists!")
