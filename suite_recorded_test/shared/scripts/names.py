# encoding: UTF-8

from objectmaphelper import *

address_Book_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": "Address Book"}
address_Book_New_QToolButton = {"text": "New", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow}
address_Book_Unnamed_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": "Address Book - Unnamed"}
address_Book_Unnamed_Add_QToolButton = {"text": "Add", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_Unnamed_MainWindow}
address_Book_Add_Dialog = {"type": "Dialog", "unnamed": 1, "visible": 1, "windowTitle": "Address Book - Add"}
address_Book_Add_Forename_QLabel = {"text": "Forename:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
forename_LineEdit = {"buddy": address_Book_Add_Forename_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_Surname_QLabel = {"text": "Surname:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
surname_LineEdit = {"buddy": address_Book_Add_Surname_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_Email_QLabel = {"text": "Email:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
email_LineEdit = {"buddy": address_Book_Add_Email_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_Phone_QLabel = {"text": "Phone:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
phone_LineEdit = {"buddy": address_Book_Add_Phone_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_OK_QPushButton = {"text": "OK", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
address_Book_Unnamed_File_QToolBar = {"type": "QToolBar", "unnamed": 1, "visible": 1, "window": address_Book_Unnamed_MainWindow, "windowTitle": "File"}
address_Book_Unnamed_File_QTableWidget = {"aboveWidget": address_Book_Unnamed_File_QToolBar, "type": "QTableWidget", "unnamed": 1, "visible": 1, "window": address_Book_Unnamed_MainWindow}
file_0_0_QModelIndex = {"column": 0, "container": address_Book_Unnamed_File_QTableWidget, "row": 0, "type": "QModelIndex"}
file_0_1_QModelIndex = {"column": 1, "container": address_Book_Unnamed_File_QTableWidget, "row": 0, "type": "QModelIndex"}
file_0_2_QModelIndex = {"column": 2, "container": address_Book_Unnamed_File_QTableWidget, "row": 0, "type": "QModelIndex"}
file_0_3_QModelIndex = {"column": 3, "container": address_Book_Unnamed_File_QTableWidget, "row": 0, "type": "QModelIndex"}
