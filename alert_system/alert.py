import smtplib
from email.mime.text import MIMEText

def send_alert(subject, body, to):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = to

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.sendmail('your_email@example.com', to, msg.as_string())

# Example usage
if __name__ == "__main__":
    send_alert("Anomaly Detected", "An anomaly was detected in the system.", "recipient@example.com")
