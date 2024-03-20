# -*- coding: utf-8 -*-

from names import *


def main():
    startApplication("addressbook")
    
    addressBook = MainPage()
    addressBook.newAddressBook()
    addressBook.addContact()
    
    addPage = AddPage()
    addPage.typeInto(addPage.forename_LineEdit, 'test1')
    addPage.typeInto(addPage.surname_LineEdit, 'test2')
    addPage.typeInto(addPage.email_LineEdit, 'test3')
    addPage.typeInto(addPage.phone_LineEdit, 'test4')
    addPage.ok()
    
    test.compare(waitForObjectExists(MainPage.forename_cell).text, "test1")
    test.compare(waitForObjectExists(MainPage.surname_cell).text, "test2")
    test.compare(waitForObjectExists(MainPage.email_cell).text, "test3")
    test.compare(waitForObjectExists(MainPage.phone_cell).text, "test4")