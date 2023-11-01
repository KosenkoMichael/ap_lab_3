import csv
import time
import os


def file_cut_date_and_data(path: str, folder: str) -> None:
    """open file and cut it on 2 files (file with data and file with date)"""
    date = []
    data = []
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            date.append([row[0]])
            data.append([row[i] for i in range(1, 7)])
    with open(f"{folder}\\X.csv", "w", encoding="utf-8", newline="") as file_x:
        writer = csv.writer(file_x)
        writer.writerows(date)
    with open(f"{folder}\\Y.csv", "w", encoding="utf-8", newline="") as file_y:
        writer = csv.writer(file_y)
        writer.writerows(data)
    print("end")


def find_data_dataset(path: str, data: str) -> tuple:
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if data == row[0]:
                mass = []
                for i in range(1, len(row)):
                    mass.append(row[i])
                return (data, mass)
        return None


def find_data_datA_E(path_X: str, path_Y: str, data: str) -> tuple:
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
        return None


def find_data_years(path: str, data: str) -> tuple:
    for year in range(2008, 2024):
        with open(f"{path}\\{year}0101-{year}1231.csv", "r", encoding="utf-8", newline="") as file_N:
            reader = csv.reader(file_N)
            for row in reader:
                if data == row[0]:
                    mass = []
                    for i in range(1, len(row)):
                        mass.append(row[i])
                    return (data, mass)
        time.sleep(0.1)
    return None


def find_data_weeks(path: str, data: str) -> tuple:
    file_names = os.listdir(path)
    for file_name in file_names:
        file_path = os.path.join(path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if data == row[0]:
                        mass = []
                        for i in range(1, len(row)):
                            mass.append(row[i])
                        return str(mass)
    return None


def N_cut_by_week(path: str, folder: str):
    day_x = ""
    for year in range(2008, 2024):
        for month in range(1, 12):
            for i in range(0, 5):
                with open(f"{path}", "r", encoding="utf-8", newline="") as file:
                    reader = csv.reader(file)
                    data = []
                    for row in reader:
                        for day in range(1+7*i, 8+7*i):
                            if str(day).zfill(2) == row[0][0]+row[0][1] and str(month).zfill(2) == row[0][3]+row[0][4] and str(year).zfill(4) == row[0][6]+row[0][7]+row[0][8]+row[0][9]:
                                data.append(row)
                                day_x = row[0]
                time.sleep(0.1)
                if len(data):
                    with open(f"{folder}\\{year}.{month}.{1+7*i}-{year}.{month}.{day_x}.csv", "w", encoding="utf-8", newline="") as file_N:
                        writer = csv.writer(file_N)
                        writer.writerows(data)
                time.sleep(0.1)
    print("end")


def N_cut_by_year(path: str, folder: str) -> None:
    """open file and cut it on N files (1file = 1year)"""
    for year in range(2008, 2024):
        data = []
        with open(path, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if f".{year}" in row[0]:
                    data.append(row)
        time.sleep(0.1)
        with open(f"{folder}\\{year}0101-{year}1231.csv", "w", encoding="utf-8", newline="") as file_N:
            writer = csv.writer(file_N)
            writer.writerows(data)
        time.sleep(0.1)
    print("end")


class Iterator:
    def __init__(self, limit, path):
        self.limit = limit
        self.counter = 0
        self.path = path

    def __iter__(self):
        return self

    def __next__(self):
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
            raise StopIteration


def next_iter(path: str) -> tuple:
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            data = row[0]
            mass = []
            for i in range(1, len(row)):
                mass.append(row[i])
            yield (data, mass)
