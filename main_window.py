import sys
import os
from os import path
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication, QMainWindow)
from design import Ui_MainWindow
import lib


class Weather(QMainWindow):
    def __init__(self):
        main_path = ""
        datae_path = ""
        years_path = ""
        weaks_path = ""
        iter = ""
        super(Weather, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.main_file.clicked.connect(self.select_main_filepath)
        self.ui.folder_for_datae.clicked.connect(
            self.select_folder_for_datae)
        self.ui.folder_for_years.clicked.connect(
            self.select_folder_for_years)
        self.ui.folder_for_weaks.clicked.connect(
            self.select_folder_for_weaks)
        self.ui.find_years.clicked.connect(self.get_data_years)
        self.ui.find_weaks.clicked.connect(self.get_data_weaks)
        self.ui.find_datae.clicked.connect(self.get_data_datae)
        self.ui.cut_datae.clicked.connect(self.cut_by_datae)
        self.ui.cut_years.clicked.connect(self.cut_by_years)
        self.ui.cut_weaks.clicked.connect(self.cut_by_weaks)
        self.ui.get_next.clicked.connect(self.show_next)

    def show_next(self) -> None:
        """iterator in main dataset
        """
        try:
            self.ui.label.setText(str(next(self.iter)))
        except:
            self.ui.label.setText("no file iterate")

    def select_main_filepath(self) -> None:
        """select path for original dataset
        """
        filepath = QtWidgets.QFileDialog.getOpenFileName(self, 'Select File')[0]
        if ".csv" == path.splitext(filepath)[1]:
            self.main_path = filepath
            self.iter = lib.Iterator(filepath)
            self.ui.label.setText("")
        else:
            self.ui.label.setText("Chosen file needs to be .csv")
    def select_folder_for_datae(self) -> None:
        """select filepath for data/date cut
        """
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Select Folder')
        self.datae_path = folderpath

    def select_folder_for_years(self) -> None:
        """select filepath for years cut
        """
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Select Folder')
        self.years_path = folderpath

    def select_folder_for_weaks(self) -> None:
        """select filepath for weaks cut
        """
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Select Folder')
        self.weaks_path = folderpath

    def get_data_years(self) -> None:
        """find date from Line Edit in dataset with years
        """
        try:
            cur_data = self.ui.textEdit.text()
            data = str(lib.find_data_years(self.years_path, cur_data))
            self.ui.label.setText(data)
        except:
            self.ui.label.setText("no file path")

    def get_data_weaks(self) -> None:
        """find date from Line Edit in dataset with weaks
        """
        try:
            cur_data = self.ui.textEdit.text()
            data = str(lib.find_data_weeks(self.weaks_path, cur_data))
            self.ui.label.setText(data)
        except:
            self.ui.label.setText("no file path")

    def get_data_datae(self) -> None:
        """find date from Line Edit in dataset with data/date
        """
        try:
            cur_data = self.ui.textEdit.text()
            data = str(lib.find_data_datA_E(os.path.join(self.datae_path,
                    "X.csv"), os.path.join(self.datae_path, "Y.csv"), cur_data))
            self.ui.label.setText(data)
        except:
            self.ui.label.setText("no file path")

    def cut_by_datae(self) -> None:
        """cut original dataset on data/date
        """
        try:
            lib.file_cut_date_and_data(self.main_path, self.datae_path)
        except:
            self.ui.label.setText("no file path")

    def cut_by_years(self) -> None:
        """cut original dataset on years
        """
        try:
            lib.N_cut_by_year(self.main_path, self.years_path)
        except:
            self.ui.label.setText("no file path")
    def cut_by_weaks(self) -> None:
        """cut original dataset on weaks
        """
        try:
            lib.N_cut_by_week(self.main_path, self.weaks_path)
        except:
            self.ui.label.setText("no file path")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Weather()
    window.show()
    sys.exit(app.exec())
