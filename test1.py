# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# import pandas as pd
# from email.mime.text import MIMEText
# import base64

# SCOPES = ['Your Gmail API scope here']

# def gmail_authenticate():
#     flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#     creds = flow.run_local_server(port=0)
#     service = build('gmail', 'v1', credentials=creds)
#     return service


# # we are reading from the csv file and taking out data by pandas
# def create_message(to, subject, body_text):
#     message = MIMEText(body_text)
#     message['to'] = to
#     message['subject'] = subject
#     raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
#     return {'raw': raw}

# def send_emails(service, csv_path):
#     df = pd.read_csv(csv_path)
#     for index, row in df.iterrows():
#         email = row['professor_emails']
#         name = row['professor_names']
#         body = f"""Respected XYZ,
#         I am interested in applying for the scholarship that your department is currently offering.I am an undergraduate student of Computer Engineering at UET Lahore.I have attached my detailed resume along with my certificates and research papers below.Kindly review them because I think I am a potential candidate for this scholarship.I would love to work with you on your upcoming research.
#         Best regards,
#         Fatima"""
#         body = body.replace("XYZ", name)
#         message = create_message(email, "Application For Scholarship", body)
#         service.users().messages().send(userId="me", body=message).execute()

# if __name__ == '__main__':
#     service = gmail_authenticate()
#     send_emails(service, 'Book1.csv')



# form no 2


from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pandas as pd
from email.mime.text import MIMEText
import base64
import google.generativeai as genai  # Gemini API

SCOPES = ['your gmail api scope here']


genai.configure(api_key="your api key here")  

def gmail_authenticate():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('gmail', 'v1', credentials=creds)
    return service

def create_message(to, subject, body_text):
    message = MIMEText(body_text)
    message['to'] = to
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}




def generate_email(name):
    prompt = f"""Write a polite email to Professor {name} expressing interest in their upcoming scholarship offer on and asking about scholarship opportunities. Mention that I am a student from Pakistan studying Computer Engineering at UET Lahore, and I have attached my resume and research papers."""
    model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text


def send_emails(service, csv_path):
    df = pd.read_csv(csv_path)
    for index, row in df.iterrows():
        email = row['professor_emails']
        name = row['professor_names']
        body = generate_email(name)
        message = create_message(email, "Application For Scholarship", body)
        service.users().messages().send(userId="me", body=message).execute()

if __name__ == '__main__':
    service = gmail_authenticate()
    send_emails(service, 'Book1.csv')





