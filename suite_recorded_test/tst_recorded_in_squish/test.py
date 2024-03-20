# -*- coding: utf-8 -*-

import names


def main():
    startApplication("addressbook")
    clickButton(waitForObject(names.address_Book_New_QToolButton))
    clickButton(waitForObject(names.address_Book_Unnamed_Add_QToolButton))
    type(waitForObject(names.forename_LineEdit), "test1")
    mouseClick(waitForObject(names.surname_LineEdit), 16, 7, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.surname_LineEdit), "test2")
    mouseClick(waitForObject(names.email_LineEdit), 23, 16, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.email_LineEdit), "test3")
    mouseClick(waitForObject(names.phone_LineEdit), 28, 10, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.phone_LineEdit), "test4")
    clickButton(waitForObject(names.address_Book_Add_OK_QPushButton))
    test.compare(waitForObjectExists(names.file_0_0_QModelIndex).text, "test1")
    test.compare(waitForObjectExists(names.file_0_1_QModelIndex).text, "test2")
    test.compare(waitForObjectExists(names.file_0_2_QModelIndex).text, "test3")
    test.compare(waitForObjectExists(names.file_0_3_QModelIndex).text, "test4")
