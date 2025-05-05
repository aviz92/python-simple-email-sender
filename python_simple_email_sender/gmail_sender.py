import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


class EmailSender:
    def __init__(
        self,
        server_name: str = 'smtp.gmail.com',
        server_port: int = 465
    ):
        self.logger = logging.getLogger(self.__class__.__name__)

        self.server_name = server_name
        self.server_port = server_port

        self.email_address = os.getenv('EMAIL_ADDRESS')
        self.email_password = os.getenv('EMAIL_PASSWORD')

        self.msg = None

    def add_attachment(self, attachment_file: str, subtype: str = 'txt') -> None:
        with open(attachment_file, 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype=subtype)
            attachment.add_header(
                _name='Content-Disposition',
                _value='attachment',
                filename=attachment_file.split('/')[-1]
            )
            self.msg.attach(attachment)

    def send_email(self, to_email: list, subject: str, message: str, attachment_file: str = None) -> None:
        self.msg = MIMEMultipart(message)
        self.msg['From'] = self.email_address
        self.msg['To'] = ', '.join(to_email)
        self.msg['Subject'] = subject

        text = MIMEText(message)
        self.msg.attach(text)

        if attachment_file:
            self.add_attachment(attachment_file)

        try:
            with smtplib.SMTP_SSL(self.server_name, self.server_port) as smtp_server:
                smtp_server.login(self.email_address, self.email_password)
                smtp_server.sendmail(from_addr=self.email_address, to_addrs=to_email, msg=self.msg.as_string())
                self.logger.info("Email sent successfully!")
        except Exception as e:
            self.logger.error(f"Email sending failed. Error: {str(e)}\n\n")
            self.logger.exception('')
