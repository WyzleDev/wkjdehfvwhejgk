from win32com import client
import time
import pythoncom


def printWordDocument(filename):
    pythoncom.CoInitialize()
    word = client.Dispatch("Word.Application")
    print(filename)       
    word.Documents.Open(filename)
    word.ActiveDocument.PrintOut()
    word.ActiveDocument.Close()
    word.Quit()
    



