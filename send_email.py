import smtplib

sender = ""
receiver = ""
password = ""
subject = "Python email test"
body = "This is the body of the email"

#header
message = f""" From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gamil.com",587)
server.starttls()

try:
    server.login(sender,password)
    print("logged in....")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("Invalid login credentials")