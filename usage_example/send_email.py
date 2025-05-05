import logging
from custom_python_logger.logger import get_logger

from python_simple_email_sender.gmail_sender import EmailSender


def main():
    logger = get_logger(
        project_name='Gmail Sender',
        log_level=logging.DEBUG,
        extra={'user': 'test_user'}
    )

    # Initialize the GmailSender with your Gmail credentials
    sender = EmailSender()

    # Compose and send an email with an optional attachment
    _to_email = ['to_example@gmail.com']
    _subject = 'Hello, recipient!'
    _message = 'This is a test email from Python.'

    # Specify the attachment file path or leave it as None if no attachment is needed
    _attachment_file = None

    sender.send_email(
        to_email=_to_email,
        subject=_subject,
        message=_message,
        attachment_file=_attachment_file
    )


if __name__ == "__main__":
    main()
