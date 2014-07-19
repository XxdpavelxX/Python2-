"""Here are your instructions:


Write a program that imports the following names from a "settings" module:
RECIPIENTS   a list of (name, email-address) tuples
STARTTIME    datetime.datetime object for first message
DAYCOUNT    number of daily message generations

The program should produce a message of the format:
Date: {{date}}
From: website@example.com
To: {{recipient}}
Message-Id: <NNNNNN>

This is a test message.
Your program should save these messages in the messages table.


Use test-driven development, and state the purpose of each test in the suite in docstrings that will eventually 
document your program.

 Time your program for DAYCOUNTS of 1, 10, 50, 100, and 500 and plot the results (on a sheet of paper). How reliable
 are the timings? 

Think of it like this: You are soon to go on vacation, at STARTTIME, for DAYCOUNT days, and you want your co-workers
(RECIPIENTS) to continue getting your famous Joke of the Day (JOTD).

Your strategy is to store up the emails ahead of time, predated with the date they're to be sent. So if you leave on 
vacation on Jan 3, 2013, the first set of emails might be dated Jan 4 (each recipient gets one), then Jan 5 and so on,
for DAYCOUNT days.

A good test that you have the right number is DAYCOUNT * len(RECIPIENTS) should equal SELECT COUNT(*) FROM jotd_emails; 
that is, the total number of days you're on vacation times the number of receivers, should equal the total number of 
records in the table generated. Of course, this will only be true if your To: line is only to a single recipient, and
not all of them separated by commas.

Storing the right date for each email will likely involve using a timedelta to increment a datetime by one day at a time
for DAYCOUNT days.

Regarding timing, it's enough to count under your breath and give a sense in your remarks about how you think time
might be a function of DAYCOUNT. If you have your email generating and storing function where you might conveniently go:
    start = time.time()
    call_function(args)
    end = time.time()
    interval = end - start
    print("Time to complete: ", end)

Then you could also give some hard numbers as to the relative times the program took as a function of changing 
DAYCOUNT. The purpose of this requirement is to look ahead to future projects where timing / profiling is a core focus.
"""

##############################################################################################################################################################################

'''
Created on Jul 3, 2014
@author: pdvorkin
Written with Python 3

Python2: Final Project
Email Search and Display
'''


from database import login_info
from email.utils import make_msgid, formatdate, formataddr, parsedate_tz, mktime_tz
from email import message_from_string
from datetime import datetime, timedelta
import time
from database import login_info
from email import message_from_string
import mysql.connector
from settings import RECIPIENTS, STARTTIME, DAYCOUNT

 
def message_maker(recipients, starttime, daycount):
    """Makes/saves messages in a list as specified by settings"""
 
    date = starttime
    msg_list = []
    for i in range(daycount):
        for recipient in recipients:
            msg = message_from_string("This is a test message.")
            # Changing from RFC settings to datetime setting.
            msg["Date"] = formatdate(time.mktime(date.timetuple()), localtime=True)
            msg["From"] = "website@example.com"
            msg["To"] = formataddr(recipient)
            msg["Message-ID"] = make_msgid()
            msg_list.append(msg)
        date = date + timedelta(days=1)  # increment date by one day
    return msg_list
 
def message_saver(msg_list):
    """Puts list of msgs into SQL database table."""
    db = mysql.connector.Connect(**login_info)
    cursor = db.cursor()
    for msg in msg_list:
        date = datetime.fromtimestamp(mktime_tz(parsedate_tz(msg["Date"])))
        #cursor.execute("""CREATE TABLE IF NOT EXISTS message (msgMessageID VARCHAR(128), msgDate DATETIME, msgRecipient VARCHAR(128),msgText LONGTEXT""")
        cursor.execute("""INSERT INTO message (msgMessageID, msgDate, msgRecipient,
                      msgText) VALUES (%s, %s, %s, %s)""",
                       (msg["Message-ID"], date, msg["To"], msg.as_string()))
    db.commit()
 
if __name__ == "__main__":
    start = time.time()
    a= message_maker(RECIPIENTS, STARTTIME, DAYCOUNT)
    message_saver(a)
    end = time.time()
    print("Duration:", end - start) # Calculates how long it takes the program to run
