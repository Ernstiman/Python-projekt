from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'viktor@ekastigen.net'
email_password = 'snff yevb nkau pemq'
email_receiver = 'viktor@ekastigen.net'

subject = '<3'

em = EmailMessage()
em['from'] = email_sender
em['to'] = email_receiver
em['Subject'] = subject
html = f"""
<html>
  <body>
    <img src ='https://media.tenor.com/sLnZKOGknYUAAAAC/hug-love.gif'>
   
  
  </body>
</html>
"""
em.add_alternative(html, subtype = "html")

context = ssl.create_default_context()  

def mail():
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    
