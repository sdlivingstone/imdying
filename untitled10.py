import smtplib 
to = '8482194611@tmomail.net'
gmail_user = "goannabananasavana@gmail.com"
gmail_pwd = "U7CWbg4wJkrmXB"

smtpserver = smtplib.SMTP ("smtp.gmail.com",587)

smtpserver.ehlo()
smtpserver.startls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)

header= 'To:DAN' + to + '\n' + 'From:SHAN' + gmail_user + '\n' + 'Subject: ANNOYING \n'
print(header)
msg=header + '\n HOLA \n\n'
smtpserver.sendmail (gmail_user,to, msg)

print ('Done!')
smtpserver.close()