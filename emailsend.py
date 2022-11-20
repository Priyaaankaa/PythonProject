from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'priyankanetcore53@gmail.com'
password = 'vrfsxcggolvhmxzo'

email_reciever = 'votor21984@invodua.com'
subject = 'Hurray! First Python Project'
body = """ Hi, so I am really very excited to start learning Python on my own. This is completely research based ad I am so keen to learn about all the cool libs and packages that python has in store for me. \n Hopefully this will change my attitude towards coding and make my weekends fun and productive \n Regards, \n Priyanka. """

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())