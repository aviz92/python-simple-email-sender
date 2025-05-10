# Python Simple Email Sender
A lightweight Python library for sending emails with attachments via SMTP.

---

## Features
- Send emails using SMTP protocol
- Support for SSL encryption
- Add attachments to emails
- Environment variable based configuration
- Simple logging integration

---

## Installation
```bash
pip install python_simple_email_sender
```

---

## Usage

### Basic Setup
First, set up your email credentials as environment variables:
```bash
export EMAIL_ADDRESS="your.email@gmail.com"
export EMAIL_PASSWORD="your-app-password-or-email-password"
```

> **Note:** For Gmail accounts, you may need to use an App Password instead of your regular password, especially if you have 2-factor authentication enabled.
> https://myaccount.google.com/apppasswords
---

### Simple Example
```python
from python_simple_email_sender import EmailSender

# Create an instance with default settings (Gmail SMTP)
sender = EmailSender()

# Send a simple email
sender.send_email(
    to_email=["recipient@example.com"],
    subject="Hello from Python",
    message="This is a test email sent using Python Simple Email Sender."
)
```

### Custom SMTP Server
```python
# For a different email provider
sender = EmailSender(
    server_name="smtp.yourprovider.com",
    server_port=587  # Use the appropriate port for your provider
)
```

### Sending with Attachments
```python
sender.send_email(
    to_email=["recipient@example.com", "another@example.com"],
    subject="Report Attached",
    message="Please find the attached report.",
    attachment_file="path/to/your/file.pdf"
)
```

### Adding Multiple Attachments
```python
sender = EmailSender()

# Create the email
sender.msg = MIMEMultipart()
sender.msg['From'] = sender.email_address
sender.msg['To'] = 'recipient@example.com'
sender.msg['Subject'] = 'Multiple Attachments'

# Add message body
text = MIMEText("Here are the files you requested.")
sender.msg.attach(text)

# Add multiple attachments
sender.add_attachment("document.pdf", subtype="pdf")
sender.add_attachment("data.csv", subtype="csv")
sender.add_attachment("image.png", subtype="png")

# Send the email
with smtplib.SMTP_SSL(sender.server_name, sender.server_port) as smtp_server:
    smtp_server.login(sender.email_address, sender.email_password)
    smtp_server.sendmail(
        from_addr=sender.email_address, 
        to_addrs=['recipient@example.com'], 
        msg=sender.msg.as_string()
    )
```

---

## 🤝 Contributing
If you have a helpful tool, pattern, or improvement to suggest:
Fork the repo <br>
Create a new branch <br>
Submit a pull request <br>
I welcome additions that promote clean, productive, and maintainable development. <br>

---

## 🙏 Thanks
Thanks for exploring this repository! <br>
Happy coding! <br>
