__author__ = 'Lieven'

import mandrill

import sys
import csv


def execute(row):
    mandrill_client = mandrill.Mandrill(row['ApiKey'])
    messages = mandrill.Messages(mandrill_client)
    messages.send_raw(row['Message'], row['FromEmail'], row['FromName'], row['ToEmail'])

def show_params():
    return "ApiKey,Message,FromEmail,FromName,ToEmail\n"



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

