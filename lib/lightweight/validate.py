import os
import shutil
import zipfile
import smtplib
import configparser
from datetime import datetime

def zip_directory(directory_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(directory_path):
            for file in files:
                zipf.write(os.path.join(root, file), 
                           os.path.relpath(os.path.join(root, file), 
                           os.path.join(directory_path, '..')))

def email_zip(zip_path, recipient_email):
    config = configparser.ConfigParser()
    config.read('../config.ini')
    
    sender_email = config['EMAIL']['SENDER']
    sender_password = config['EMAIL']['PASSWORD']
    smtp_server = config['EMAIL']['SMTP_SERVER']
    smtp_port = config['EMAIL']['SMTP_PORT']

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        with open(zip_path, 'rb') as f:
            file_data = f.read()
        message = f"""\
Subject: Zipped Repo Data
To: {recipient_email}
From: {sender_email}

Please find the attached zip file containing the repo data.
"""
        server.sendmail(sender_email, recipient_email, message, file_data)

def main():
    base_path = 'repo_data'
    current_date = datetime.now().strftime('%Y-%m-%d')
    zip_path = f"{base_path}-{current_date}.zip"
    recipient_email = input("Enter recipient email: ")

    zip_directory(base_path, zip_path)
    email_zip(zip_path, recipient_email)

    shutil.rmtree(base_path)

if __name__ == "__main__":
    main()