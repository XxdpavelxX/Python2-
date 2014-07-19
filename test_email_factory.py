'''
Created on Jul 3, 2014
@author: pdvorkin
Written with Python 3

Python2: Final Project
Testing Email Search and Display Program
'''


"""Lesson 13: Email Search and Display, Project 1 - testing module"""
 
from database import login_info
from settings import RECIPIENTS, STARTTIME, DAYCOUNT
from email.utils import formataddr
from email_factory import message_maker, message_saver
import unittest
import mysql.connector
 
db = mysql.connector.Connect(**login_info)
cursor = db.cursor()
 
TBLDEF = """
CREATE TABLE message (
   msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
   msgMessageID VARCHAR(128),
   msgDate DATETIME,
   msgRecipient VARCHAR(128),
   msgText LONGTEXT
)"""
 
class TestEmailgen(unittest.TestCase):
    def setUp(self):
        """Creates a database table into which messages are saved"""
 
        cursor.execute("DROP TABLE IF EXISTS message")
        db.commit()
        cursor.execute(TBLDEF)
        db.commit()
        message_saver(message_maker(RECIPIENTS, STARTTIME, DAYCOUNT))
 
    def testMessageAmount(self):
        """Checks if the correct amount of messages has been saved"""
 
        cursor.execute("SELECT COUNT(*) FROM message")
        amount = cursor.fetchone()[0]
        expected = DAYCOUNT * len(RECIPIENTS)
        self.assertEqual(amount, expected, "The amount of saved messages is incorrect.")
 
    def testRecipients(self):
        """Makes sure the daily messages are addressed to all of the recipients"""
 
        cursor.execute("SELECT msgRecipient FROM message WHERE msgDate = %s", (STARTTIME,))
        recipients = set()
        for row in cursor.fetchall():
            recipients.add(row[0])
        expected = set([formataddr(each) for each in RECIPIENTS])
        self.assertEqual(recipients, expected,
                         "Messages are not addressed to all of the recipients.")
 
if __name__ == "__main__":
    unittest.main()

