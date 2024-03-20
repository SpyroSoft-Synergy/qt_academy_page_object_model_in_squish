# -*- coding: utf-8 -*-

import squish
import test

class MainPage():
    
    address_Book_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": "Address Book"}
    address_Book_New_QToolButton = {"text": "New", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow}
    address_Book_Unnamed_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": "Address Book - Unnamed"}
    address_Book_Unnamed_Add_QToolButton = {"text": "Add", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_Unnamed_MainWindow}
    address_Book_Unnamed_File_QToolBar = {"type": "QToolBar", "unnamed": 1, "visible": 1, "window": address_Book_Unnamed_MainWindow, "windowTitle": "File"}
    address_Book_Unnamed_File_QTableWidget = {"aboveWidget": address_Book_Unnamed_File_QToolBar, "type": "QTableWidget", "unnamed": 1, "visible": 1, "window": address_Book_Unnamed_MainWindow}
    forename_cell = {"column": 0, "container": address_Book_Unnamed_File_QTableWidget, "row": 0, "type": "QModelIndex"}
    surname_cell = {"column": 1, "container": address_Book_Unnamed_File_QTableWidget, "row": 0, "type": "QModelIndex"}
    email_cell = {"column": 2, "container": address_Book_Unnamed_File_QTableWidget, "row": 0, "type": "QModelIndex"}
    phone_cell = {"column": 3, "container": address_Book_Unnamed_File_QTableWidget, "row": 0, "type": "QModelIndex"}
    
    def __init__(self):
        test.verify(squish.waitForObject(self.address_Book_MainWindow), 'Verify if main page is displayed')
    
    def newAddressBook(self):
        squish.clickButton(squish.waitForObject(self.address_Book_New_QToolButton))
        
    def addContact(self):
        squish.clickButton(squish.waitForObject(self.address_Book_Unnamed_Add_QToolButton))