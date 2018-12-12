import sys
import csv
import datetime

__author__ = 'lveeckha'


def execute(row):
        recipients = row['ToEmails']
        subject = row['Subject']
        ddtstart = datetime.datetime.strptime(row['StartTime'], "%Y-%m-%d")
        dtend = datetime.datetime.strptime(row['EndTime'], "%Y-%m-%d")
        dtstamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%SZ")
        dtstart = ddtstart.strftime("%Y%m%dT%H%M%SZ")
        dtend = dtend.strftime("%Y%m%dT%H%M%SZ")
        organizer = row['FromEmail']
        CRLF="\n"
        description = "DESCRIPTION: " + subject + CRLF
        attendee = ""
        for att in recipients.split(";"):
            attendee += "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-    PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE" + CRLF + " ;CN=" + att + ";X-NUM-GUESTS=0:" + CRLF + " mailto:" + att + CRLF
        ical = "BEGIN:VCALENDAR" + CRLF + "PRODID:pyICSParser" + CRLF + "VERSION:2.0" + CRLF + "CALSCALE:GREGORIAN" + CRLF
        ical += "METHOD:REQUEST" + CRLF + "BEGIN:VEVENT" + CRLF + "DTSTART:" + dtstart + CRLF + "DTEND:" + dtend + CRLF + "DTSTAMP:" + dtstamp + CRLF + organizer + CRLF
        ical += "UID:FIXMEUID" + dtstamp + CRLF
        ical += attendee + "CREATED:" + dtstamp + CRLF + description + "LAST-MODIFIED:" + dtstamp + CRLF + "LOCATION:" + CRLF + "SEQUENCE:0" + CRLF + "STATUS:CONFIRMED" + CRLF
        ical += "SUMMARY: " + row['DescriptionHTML'] + CRLF + "TRANSP:OPAQUE" + CRLF + "END:VEVENT" + CRLF + "END:VCALENDAR" + CRLF

        with open(row['Filename'], 'w') as outfile:
            outfile.write(ical)

def show_params():
    return "FromEmail, ToEmails,cc Emails,Subject,DescriptionHTML, Start Time, End Time, Filename\nEmails,Start Time, End time"



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