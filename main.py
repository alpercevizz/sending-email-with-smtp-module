import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

message = MIMEMultipart() #create a mail structure
message["From"] = "youremail@email.com"
message["To"] = "heremail@email.com"
message["Subject"] = "Test Subject"

content = "Test content..."
message_body = MIMEText(content,"plain") #create a message body
message.attach(message_body) # message body added to message

#Connecting Gmail Server with SMTP

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587) #Gmail SMTP and port value
    mail.ehlo() # connect to smtp server
    mail.startls() #encrypted your gmail user information (email address and password)
    mail.login("youremail@email.com","your_password") #logged in gmail with email and password
    mail.sendmail(message["From"], message["To"], message.as_string()) # sending your email
    print("Mail sended successfully...")
    mail.close() #finish connecting from smtp server

except:
    sys.stderr.write("Error!!!")
    sys.stderr.flush()