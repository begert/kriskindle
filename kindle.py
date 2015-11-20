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

def testKindleMail(to, kindle):
    print kindle + ' would be sent to ' + to

def sendKindleMail(to, kindle):
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

shuffeled_kindles = list(kindles)
same = 1;
while same == 1:
    same = 0
    random.shuffle(shuffeled_kindles)
    for index, kindle in enumerate(shuffeled_kindles):
        if kindles[index] == kindle:
           same = 1

for index, kindle in enumerate(shuffeled_kindles):
    testKindleMail(kindles[index][0], kindle[1])
    #sendKindleMail(kindles[index][0], kindle[1])
