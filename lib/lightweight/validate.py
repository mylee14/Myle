import os
import shutil
import zipfile
import smtplib
import configparser

def zip_directory(directory_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(directory_path):
            for file in files:
                zipf.write(os.path.join(root, file), 
                           os.path.relpath(os.path.join(root, file), 
                           os.path.join(directory_path, '..')))

def email_zip(zip_path, recipient_email):
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    sender_email = config['EMAIL']['SENDER']
    sender_password = config['EMAIL']['PASSWORD']
    smtp_server = config['EMAIL']['SMTP_SERVER']
    smtp_port = config['EMAIL']['SMTP_PORT']

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        with open(zip_path, 'rb') as f:
            content = f.read()
        server.sendmail(sender_email, recipient_email, content)

def main():
    base_path = 'repo_data'
    zip_path = f"{base_path}-{time.strftime('%Y%m%d')}.zip"
    recipient_email = input("Enter recipient email: ")

    zip_directory(base_path, zip_path)
    email_zip(zip_path, recipient_email)

    shutil.rmtree(base_path)
    os.makedirs(base_path, exist_ok=True)

if __name__ == "__main__":
    main()