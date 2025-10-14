from dotenv import load_dotenv

from python_simple_email_sender.gmail_sender import EmailSender

load_dotenv()

__all__ = ["EmailSender"]
