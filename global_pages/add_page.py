# -*- coding: utf-8 -*-

import squish
import test

class AddPage():
    
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
    
    def __init__(self):
        test.verify(squish.waitForObject(self.address_Book_Add_Dialog), 'Verify if Add Page is displayed')
        
    def ok(self):
        squish.clickButton(squish.waitForObject(self.address_Book_Add_OK_QPushButton))
        
    def typeInto(self, locator, text):
        squish.type(locator, text)