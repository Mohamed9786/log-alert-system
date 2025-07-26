import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

def send_email_alert(subject, summary, full_log, sender, password, recipient):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject

        body = f"🛑 Log Alert Summary 🛑\n\n{summary}\n\n---\nFull Log Matches:\n\n{full_log}"
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)

        logging.info("Email alert sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
