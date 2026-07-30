import os
import smtplib

class NotificationManager:
    def __init__(self):
        self.smtp_address = "smtp.gmail.com"
        self.email = os.environ["MY_EMAIL"]
        self.password = os.environ["MY_APP_PASSWORD"]

    def send_email(self, message_body):
        with smtplib.SMTP(self.smtp_address, 587) as connection:
            connection.starttls()
            connection.login(self.email, self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=os.environ["RECIPIENT_EMAIL"],
                msg=f"Subject: Low Price Flight Alert!\n\n{message_body}".encode("utf-8")
            )
        print("Flight deal email sent successfully!")