# here we are going to build a simple smtp server using python's built in smtp library
import os
import smtplib
from dotenv import load_dotenv

load_dotenv() # load environment variables from .env file

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

# we are going to use the gmail smtp server to send an email
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
  smtp.ehlo() # identify ourselves to the server
  smtp.starttls() # encrypt our connection
  smtp.ehlo() # re-identify ourselves as an encrypted connection
  
  smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD) # login to our email account
  
  reciever_email = '24012011070@gnu.ac.in'
  subject = 'SMTP Test mail'
  body = 'This is a test email sent using Python SMTP library on the vs code directly not with the terminal .'

  msg = f'Subject: {subject}\n\n{body}' # create the email message

  smtp.sendmail(EMAIL_ADDRESS,reciever_email,msg) # sed the email to the reciptent 