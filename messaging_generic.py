'''
SMS GATEWAYS
--------------------------------------------------------------------------------
AT&T: [number]@txt.att.net
Sprint: [number]@messaging.sprintpcs.com or [number]@pm .sprint.com
T-Mobile: [number]@tmomail.net
Verizon: [number]@vtext.com
Boost Mobile: [number]@myboostmobile.com
Cricket: [number]@sms.mycricket.com
Metro PCS: [number]@mymetropcs.com
Tracfone: [number]@mmst5.tracfone.com
U.S. Cellular: [number]@email.uscc.net
Virgin Mobile: [number]@vmobl.com
'''
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# CONSTANTS
YOUR_NUMBER = ''
YOUR_EMAIL = ''
YOUR_SMS_GATEWAY = ''

# USED AS FROM
gmail_user = '' # (You should provide your gmail account name)
gmail_pwd = '' # (You should provide your gmail password)
# NOTE: gmail account must have 'Less Secure APP Access' enabled


def send_text(number, host, subject, msg):
        # CREATE CONNECTION TO SMTP SERVICE
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(gmail_user, gmail_pwd)
        # CREATE MESSAGE
        recipient = number+host
        message = MIMEMultipart("alternative")
        message["From"] = gmail_user
        message["To"] = number+host
        message["Subject"] = subject+'\n'
        message.attach(MIMEText(msg+'\n', "plain"))
        # SEND MESSAGE
        smtpserver.sendmail(gmail_user, recipient, message.as_string())
        # CLOSE CONNECTION TO SMTP SERVICE
        smtpserver.close()

def send_email(to, subject, body, is_HTML=False):
        # CREATE CONNECTION TO SMTP SERVICE
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(gmail_user, gmail_pwd)
        # CREATE MESSAGE
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = gmail_user
        message["To"] = to
        if is_HTML:
            message.attach(MIMEText(body, "html"))
        else:
            message.attach(MIMEText(body, "plain"))
        # SEND MESSAGE
        smtpserver.sendmail(gmail_user, to, message.as_string())
        # CLOSE CONNECTION TO SMTP SERVICE
        smtpserver.close()


# TEXT
def send_text(subject, msg):
    send_text(YOUR_NUMBER, YOUR_HOST, subject, msg)


# EMAIL
def send_email(subject, msg, is_HTML=False):
    send_text(YOUR_EMAIL, subject, msg, is_HTML)


# EZAMPLES:
'''
send_text(YOUR_NUMBER, YOUR_HOST, 'Subject', 'Body')

send_email(YOUR_EMAIL, 'Subject', 'Body', False)

# Create HTML message
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="https://isaaclehman.github.io/">My GitHub</a>
       has many great repositories.
    </p>
  </body>
</html>
"""
send_email(YOUR_EMAIL, 'html-test-message', html, True)
'''
