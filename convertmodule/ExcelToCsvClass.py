__author__ = 'lveeckha'

import xlrd
import csv

def execute(row):
    ExcelFile = row["ExcelFile"]
    CsvFile = row["CsvFile"]
    sheetName = row["Sheet"]
    csv_from_excel(ExcelFile, CsvFile, sheetName)


def show_params():
    return "ExcelFile;CsvFile;Sheet\nExcel file.;The destination csv file;Defines which sheet you want."


def csv_from_excel(excel_file, csv_file, sheetName):

    wb = xlrd.open_workbook(excel_file)
    sh = wb.sheet_by_name(sheetName)
    your_csv_file = open(csv_file, 'w', newline='')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in list(range((sh.nrows))):
        values = sh.row_values(rownum)
        wr.writerow(values)

    your_csv_file.close()