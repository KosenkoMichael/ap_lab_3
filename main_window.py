import sys
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
        data = ""
        super(Weather, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.select_main_filepath)
        self.ui.select_pushButton_2.clicked.connect(self.select_folder_for_datae)
        self.ui.select_pushButton_3.clicked.connect(self.select_folder_for_years)
        self.ui.select_pushButton_4.clicked.connect(self.select_folder_for_weaks)
        self.ui.pushButton_5.clicked.connect(self.get_data)
    def select_main_filepath(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(self, 'Select File')
        self.main_path =  filepath
    def select_folder_for_datae(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.datae_path =  folderpath
    def select_folder_for_years(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.years_path =  folderpath
    def select_folder_for_weaks(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.weaks_path =  folderpath
    def get_data(self):
        cur_data = self.ui.textEdit.text()
        self.data = cur_data

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Weather()
    window.show()
    sys.exit(app.exec())
