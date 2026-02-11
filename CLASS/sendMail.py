import smtplib
from email.message import EmailMessage

def send_mail(sender,app_password,receiver,subject,body):
    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.set_content(body)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
    smtp.login(sender,app_password)

    smtp.send_message(msg)

    smtp.quit()

def main():
    sender_email = "devarshipimpale02@gmail.com"
    app_password = "yittwcbhqkuyycwc"
    receiver_mail = "devarshipimpale@gmail.com"
    subject = "Test Mail from Python Script"
    body = """Jay Ganesh,
This is the test email sent using Marvellous python.

Regards,
Devarshi Pimpale
    """

    send_mail(sender_email,app_password,receiver_mail,subject,body)
    print("Marvellous Mail Sent Successfully")

if __name__ == "__main__":
    main()
