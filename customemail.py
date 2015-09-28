# Import smtplib for the actual sending function
import smtplib
import os

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open('C:\Python34\Programs\writefile2.txt', 'rb')
# Create a text/plain message
msg = fp.read()
print (msg)
fp.close()
msgB = msg.decode('utf-8')
print (msgB)
msgbyte = bytearray(msg)
print (msgbyte)

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = "this is a test"
msg['From'] = 'bkbhanu@hotmail.com'
msg['To'] = 'bkbhanu@gmail.com'
username = 'bkbhanu@gmail.com'
password = 'SimpleEasy109!'
s.starttls()
s.
# Send the message via our own SMTP server.
s = smtplib.SMTP('smtp.gmail.com:587')
s.send_message(msg)
s.se
s.quit()

