"""Here are your instructions:

Write a function that takes an email address, a string, and a list argument. It should return an email message addressed
to the email address passed as the first argument,with the second argument as the message body. If the list is non-empty, 
then each list item should be treated as the name of a file and the corresponding file should be attached
(with an appropriate MIME type) to the message.

Please include any files to attach in the same folder as your program.  There is no need to send it as an email with 
smtp, though you may wish to print it as a string as a part of testing."""

###########################################################################################################################################################################

from email.mime.text import MIMEText
import email
import mimetypes
import os
from email.mime.multipart import MIMEMultipart
import email.MIMEAudio

import email.message
from email.mime.image import MIMEImage

def createMessage(address, content,list1):
    msg = MIMEMultipart()
    msg['to'] =address
    msg['from']=address
    msg['subject']='test subject'
    text_msg = MIMEText(content, 'plain')
    msg.attach(text_msg)
    dir = os.curdir
    for fn in list1:
     
        with open(fn, 'rb') as fp:
            
            path = os.path.join(dir, fn)
            if not os.path.isfile(path):
                continue
            ctype, encoding = mimetypes.guess_type(path)
            if ctype is None or encoding is not None:
                    ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/', 1)
            if maintype == 'text':
                    fp = open(path)
                    attachment = MIMEText(fp.read(), _subtype=subtype)
                    fp.close()

            elif maintype=='image':
                fp = open(path)
                attachment = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()

            elif maintype=='audio':
                fp=open(path)
                attachment = email.MIMEAudio(fp.read(),_subtype=subtype)
                fp.close()

            else:
                fp=open(path)
                attachment = email.MIMEBase.MIMEBase(maintype, subtype)
                attachment.set_payload(fp.read())
                fp.close()

        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(fn))
        msg.attach(attachment)

    return(msg)
