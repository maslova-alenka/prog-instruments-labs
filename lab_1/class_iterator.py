import csv
import os


class DateIterator:
    """Iterator for reading data from a CSV file."""
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
            with open(self.file_name, "r", encoding="utf-8") as csvfile:
                reader_object = list(csv.reader(csvfile, delimiter=","))
                if self.counter == len(reader_object):
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
            raise FileNotFoundError


class DateIteratorFromXY:
    """Iterator for reading data from X and Y CSV files."""
    def __init__(self):
        """Initialize the DateIteratorFromXY."""
        self.counter = 0
        self.x = "divide_data_output//X.csv"
        self.y = "divide_data_output//Y.csv"

    def __next__(self) -> tuple:
        """Get the next tuple of data from X and Y CSV files.
        Returns:
            tuple: A tuple of data from X and Y CSV files.

        Raises:
            StopIteration: When the end of the file is reached.
            FileNotFoundError: If the files do not exist.
        """
        if os.path.exists(self.x) and os.path.exists(self.y):
            with open(self.x, "r", encoding="utf-8") as csvfile:
                reader_object = list(csv.reader(csvfile, delimiter=","))
            if self.counter == len(reader_object):
                raise StopIteration
            elif self.counter < len(reader_object):
                self.counter += 1
                with open(self.x, "r", encoding="utf-8") as csv_file_x:
                    reader_object_x = list(csv.reader(csv_file_x, delimiter=","))
                    date = reader_object_x[self.counter][0]
                with open(self.y, "r", encoding="utf-8") as csv_file_y:
                    reader_object_y = list(csv.reader(csv_file_y, delimiter=","))
                    output = (
                        date,
                        reader_object_y[self.counter - 1][0],
                        reader_object_y[self.counter - 1][1],
                        reader_object_y[self.counter - 1][2],
                        reader_object_y[self.counter - 1][3],
                        reader_object_y[self.counter - 1][4],
                        reader_object_y[self.counter - 1][5]
                    )
                    return output
            else:
                raise FileNotFoundError


class DateIteratorFromWeeks:
    """Iterator for reading data from weekly CSV files."""
    def __init__(self):
        """Initialize the DateIteratorFromWeeks."""
        self.file_name = "data_to_weeks_output"
        self.counter = 0
        self.data = []
        if os.path.exists(self.file_name):
            for root, dirs, files in os.walk(self.file_name):
                for file in files:
                    with open(os.path.join(self.file_name, file), "r", encoding="utf-8") as csv_file:
                        dates = list(csv.reader(csv_file, delimiter=","))
                        for i in range(len(dates)):
                            self.data.append(dates[i])
        else:
            raise FileNotFoundError

    def __next__(self) -> tuple:
        """Get the next tuple of data from weekly CSV files.

        Returns:
            tuple: A tuple of data from weekly CSV files.

        Raises:
            StopIteration: When the end of the file is reached.
            FileNotFoundError: If the files do not exist.
        """
        if self.counter == len(self.data):
            raise StopIteration
        elif self.counter < len(self.data):
            self.counter += 1
            output = (
                self.data[self.counter - 1][0],
                self.data[self.counter - 1][1],
                self.data[self.counter - 1][2],
                self.data[self.counter - 1][3],
                self.data[self.counter - 1][4],
                self.data[self.counter - 1][5],
                self.data[self.counter - 1][6]
            )
            return output


class DateIteratorFromYears:
    """Iterator for reading data from yearly CSV files."""
    def __init__(self):
        """Initialize the DateIteratorFromYears."""
        self.file_name = "data_to_years_output"
        self.counter = 0
        self.data = []
        if os.path.exists(self.file_name):
            for root, dirs, files in os.walk(self.file_name):
                for file in files:
                    with open(os.path.join(self.file_name, file), "r", encoding="utf-8") as csv_file:
                        dates = list(csv.reader(csv_file, delimiter=","))
                        for i in range(len(dates)):
                            self.data.append(dates[i])
        else:
            raise FileNotFoundError

    def __next__(self) -> tuple:
        """Get the next tuple of data from yearly CSV files.

        Returns:
            tuple: A tuple of data from yearly CSV files.

        Raises:
            StopIteration: When the end of the file is reached.
            FileNotFoundError: If the files do not exist.
        """
        if self.counter == len(self.data):
            raise StopIteration
        elif self.counter < len(self.data):
            self.counter += 1
            output = (
                self.data[self.counter - 1][0],
                self.data[self.counter - 1][1],
                self.data[self.counter - 1][2],
                self.data[self.counter - 1][3],
                self.data[self.counter - 1][4],
                self.data[self.counter - 1][5],
                self.data[self.counter - 1][6]
            )
            return output
