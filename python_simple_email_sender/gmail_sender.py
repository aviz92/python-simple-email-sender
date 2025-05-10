import logging
import os
import smtplib
from pathlib import Path
from typing import Union, List, Optional
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

        if not self.email_address or not self.email_password:
            raise ValueError("EMAIL_ADDRESS and EMAIL_PASSWORD must be set in environment variables")

    def _add_attachment(self, msg: MIMEMultipart, file_path: Union[str, Path], subtype: str = 'txt') -> None:
        path = Path(file_path)
        with path.open('rb') as f:
            attachment = MIMEApplication(f.read(), _subtype=subtype)
            attachment.add_header(
                _name='Content-Disposition',
                _value='attachment',
                filename=path.name
            )
            msg.attach(attachment)

    def send_email(
        self,
        to_email: Union[str, List[str]],
        subject: str,
        message: str,
        attachment_file: Optional[Union[str, Path]] = None
    ) -> None:
        if isinstance(to_email, str):
            to_email = [to_email]

        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = ', '.join(to_email)
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        if attachment_file:
            self._add_attachment(msg, attachment_file)

        try:
            with smtplib.SMTP_SSL(host=self.server_name, port=self.server_port) as server:
                server.login(user=self.email_address, password=self.email_password)
                server.sendmail(from_addr=self.email_address, to_addrs=to_email, msg=msg.as_string())
            self.logger.info("Email sent successfully.")
        except Exception:
            self.logger.exception("Failed to send email")
