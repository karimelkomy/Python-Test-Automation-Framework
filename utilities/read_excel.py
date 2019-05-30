from openpyxl import load_workbook


class ReadFromExcel():

    def __init__(self, fileName, sheetName):
        self.workbook = load_workbook(fileName)
        self.worksheet = self.workbook[sheetName]

    def readFromExcel(self, column, row):
        cell = "{}{}".format(column, row)
        cellValue = self.worksheet[cell].value
        return cellValue
