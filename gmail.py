from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import base64
from google.oauth2 import service_account
from apiclient import errors
from httplib2 import Http
from email.mime.text import MIMEText
import base64
import json

def service_account_login():
  scopes = ['https://www.googleapis.com/auth/gmail.send']
  credentials = service_account.Credentials.from_service_account_file("client_secret.json", scopes=scopes)
  dcreds = credentials.with_subject("test subject")
  service = build('gmail', 'v1', credentials=dcreds)
  return service

def create_message(sender, to, subject, message_text):
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  raw_message = base64.urlsafe_b64encode(message.as_string().encode("utf-8"))
  return {
    'raw': raw_message.decode("utf-8")
  }

def send_message(service, user_id, message):
  """Send an email message.
  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.
  Returns:
    Sent Message.
  """
  try:
    message = (service.users().messages().send(userId=user_id, body=message).execute())
    print('Message Id: %s' % message['id'])
    return message
  except errors.HttpError as error:
    print('An error occurred: %s' % error)

# Email variables. Modify this!
EMAIL_FROM = 'cubingbot@cubingbot-279013.iam.gserviceaccount.com'
EMAIL_TO = 'tyler.geist1111@gmail.com'
EMAIL_SUBJECT = 'Hello  from Lyfepedia!'
EMAIL_CONTENT = 'Hello, this is a test\nLyfepedia\nhttps://lyfepedia.com'

service = service_account_login()
message = create_message(EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT, EMAIL_CONTENT)
print(type(message))
sent = send_message(service,'me', message)
