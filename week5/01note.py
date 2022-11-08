note = open('note.txt', 'w')
note.write('Hey, you totally need to figure out this email thing. And what were you going to call that Fawlty Towers video game???')
note.close

import smtplib

smtpObj = smtplib.SMTP(["smtp-mail.outlook.com", 587])

smtpObj.sendmail("rlsoderberg@outlook.com", "rlsoderberg@outlook.com", "note")