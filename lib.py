import csv
import time
import os
import datetime


def file_cut_date_and_data(path: str, folder: str) -> None:
    """Cut .csv file on data and date files

    Args:
        path (str): path to original dataset
        folder (str): path to folder with result .csv files
    """
    date = []
    data = []
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            date.append([row[0]])
            data.append([row[i] for i in range(1, 9)])
    with open(f"{folder}\\X.csv", "w", encoding="utf-8", newline="") as file_x:
        writer = csv.writer(file_x)
        writer.writerows(date)
    with open(f"{folder}\\Y.csv", "w", encoding="utf-8", newline="") as file_y:
        writer = csv.writer(file_y)
        writer.writerows(data)
    print("end")


def find_data_dataset(path: str, data: datetime) -> tuple | None:
    """ Function: find data in original dataset

    Args:
        path (str): path to original dataset
        data (str): date, we want to find

    Returns:
        tuple: ((date, we find), (data, we found))
    """
    try:
        with open(path, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if data == row[0]:
                    mass = []
                    for i in range(1, len(row)):
                        mass.append(row[i])
                    return (data, mass)
    except:
        return None


def find_data_datA_E(path_X: str, path_Y: str, data: datetime) -> tuple | None:
    """Find data in dataset (data, date)

    Args:
        path_X (str): path to .csv with date
        path_Y (str): path to .csv with data
        data (str): date, we want to find

    Returns:
        tuple: (date, data)
    """
    try:
        pos = 1
        with open(path_X, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if data == row[0]:
                    break
                pos += 1
        with open(path_Y, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                pos -= 1
                if pos == 0:
                    return (data, row)
    except:
        return None


def find_data_years(path: str, data: datetime) -> tuple | None:
    """Find date in dataset (years)

    Args:
        path (str): path to folder with datasets
        data (str): date, we want to find

    Returns:
        tuple: (date, data)
    """
    try:
        year = data[0:4]
        with open(f"{path}\\{year}-01-01-{year}-12-31.csv", "r", encoding="utf-8", newline="") as file_N:
            reader = csv.reader(file_N)
            for row in reader:
                if data == row[0]:
                    mass = []
                    for i in range(1, len(row)):
                        mass.append(row[i])
                    return (data, mass)
        time.sleep(0.01)
    except:
        return None


def find_data_weeks(path: str, data: datetime) -> tuple | None:
    """find date in dataset (weeks)

    Args:
        path (str): path to folder with datasets
        data (str): date, we want to find

    Returns:
        tuple: (date, data)
    """
    try:
        month = data[5:7]
        year = data[0:4]
        file_names = os.listdir(path)
        for file_name in file_names:
            file_path = os.path.join(path, file_name)
            if os.path.isfile(file_path) and month and year in file_name:
                with open(file_path, "r", encoding="utf-8", newline="") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if data == row[0]:
                            mass = []
                            for i in range(1, len(row)):
                                mass.append(row[i])
                            return (data, mass)
    except:
        return None


def N_cut_by_week(path: str, folder: str) -> None:
    """Cut original dataset to weeks

    Args:
        path (str): path to original dataset
        folder (str): path to result folder
    """
    for year in range(2008, 2024):
        for month in range(1, 13):
            for i in range(0, 5):
                with open(path, "r", encoding="utf-8", newline="") as file:
                    reader = csv.reader(file)
                    data = []
                    for row in reader:
                        for day in range(1+7*i, 8+7*i):
                            if "-".join((map(lambda x: str(x).zfill(2),  list([year, month, day])))) == row[0]:
                                data.append(row)
                time.sleep(0.01)
                if len(data):
                    with open(f"{folder}\\{year}-{month}-{data[0][0][8:10]}-{year}-{month}-{data[-1][0][8:10]}.csv", "w", encoding="utf-8", newline="") as file_N:
                        writer = csv.writer(file_N)
                        writer.writerows(data)
                time.sleep(0.01)
    print("end")


def N_cut_by_year(path: str, folder: str) -> None:
    """Cut original dataset on years

    Args:
        path (str): path to original dataset
        folder (str): path to folder with result datasets
    """
    for year in range(2008, 2024):
        data = []
        with open(path, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if str(year) in row[0]:
                    data.append(row)
        time.sleep(0.1)
        with open(f"{folder}\\{year}-01-01-{year}-12-31.csv", "w", encoding="utf-8", newline="") as file_N:
            writer = csv.writer(file_N)
            writer.writerows(data)
        time.sleep(0.1)
    print("end")


class Iterator:
    def __init__(self, path: str):
        """Initializarion

        Args:
            path (srr): path to file to iterate
        """
        with open(path, "r", encoding="utf-8", newline="") as file:
            text = file.readlines()
            self.limit = len(text)
        self.counter = 0
        self.path = path

    def __iter__(self):
        return self

    def __next__(self):
        """ Get next element

        Returns:
            tuple: if next element consist
            None: if the file has ended
        """
        if self.counter < self.limit:
            self.counter += 1
            with open(self.path, "r", encoding="utf-8", newline="") as file:
                reader = csv.reader(file)
                count = 0
                for row in reader:
                    if count == self.counter and row != "":
                        data = row[0]
                        mass = []
                        for i in range(1, len(row)):
                            mass.append(row[i])
                        return (data, mass)
                    count += 1
        else:
            return None


def next_iter(path: str) -> tuple:
    """get next date in file

    Args:
        path (str): path to dataset.csv 

    Returns:
        tuple: ((date, we find), (data, we found))

    Yields:
        Iterator[tuple]: ((date, we find), (data, we found))
    """
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            data = row[0]
            mass = []
            for i in range(1, len(row)):
                mass.append(row[i])
            yield (data, mass)
