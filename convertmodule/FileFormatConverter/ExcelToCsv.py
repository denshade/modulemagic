import xlrd

__author__ = 'lveeckha'

import sys
import csv

def execute(row):
    ExcelFile = row["ExcelFile"]
    CsvFile = row["CsvFile"]
    sheetName = row["Sheet"]
    csv_from_excel(ExcelFile, CsvFile, sheetName)


def show_params():
    return "ExcelFile,CsvFile,Sheet\nExcel file.,The destination csv file,Defines which sheet you want."


def csv_from_excel(excel_file, csv_file, sheet_name):

    wb = xlrd.open_workbook(excel_file)
    sh = wb.sheet_by_name(sheet_name)
    your_csv_file = open(csv_file, 'w', newline='', encoding="utf-8")
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in list(range((sh.nrows))):
        values = sh.row_values(rownum)
        wr.writerow(values)

    your_csv_file.close()

if len(sys.argv) != 2 or sys.argv[1] == "--inputparameters":
    print(show_params())
    sys.exit(2)
if sys.argv[1] == "--validate":
    pass
    #validate(sys.argv[2])



input_file = sys.argv[1]


with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        execute(row)