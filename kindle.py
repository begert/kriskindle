import smtplib
import getpass
import random

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

kindles = [['somename@gmail.com', 'Some Name'],
          ['othername@gmail.com', 'Other Name'],
          ['yetanothername@gmail.com', 'Yet Another Name']]
sender = 'sender@gmail.com'

print 'Please enter the password for ' + sender
pw = getpass.getpass()

def testDwarfMail(to, kindle):
    print kindle + ' would be sent to ' + to

def sendDwarfMail(to, kindle):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = to
    msg['Subject'] = 'Kris Kindle'
    message = 'Your Kris Kindle is ' + kindle
    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(sender, pw)

    mailserver.sendmail(sender, to, msg.as_string())

    mailserver.quit()

d2 = list(kindles)
same = 1;
while same == 1:
    same = 0
    random.shuffle(d2)
    for index, kindle in enumerate(d2):
        if kindles[index] == kindle:
           same = 1

for index, kindle in enumerate(d2):
    testDwarfMail(kindles[index][0], kindle[1])
    #sendDwarfMail(kindles[index][0], kindle[1])
