from email.message import EmailMessage
import ssl
import smtplib
email_sender = "tssuryamoorthy20092005@gmail.com"
email_password = "rapb gstx kajq crgp"

email_receiver = 'tawij84968@apifan.com'
subject = 'live with your life'
body = "i am a good boy"
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em['body'] = body

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
  smtp.login(email_sender,email_password)
  smtp.sendmail(email_sender,email_receiver,em.as_string())
