from datetime import datetime


import os

import win32cred
from dotenv import load_dotenv
from jose import jwt, JWTError
load_dotenv()
import requests

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
login_service = os.getenv('LOGIN_SERVICE')


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        if datetime.fromtimestamp(payload.get('exp')) < datetime.now():

            headers = {'Authorization': f'Bearer {token}'}
            new_token = requests.get(f"{login_service}/login",headers=headers)


            save_token(new_token)
            return new_token

        return token
    except JWTError:
        raise ValueError('Invalid Token')

def save_token(token):
    cred = {
        'Type': win32cred.CRED_TYPE_GENERIC,
        'TargetName': 'FinanceTr_Access_token',
        'CredentialBlob': token,
        'Persist': win32cred.CRED_PERSIST_LOCAL_MACHINE
    }

    try:
        win32cred.CredWrite(cred, 0)
        print("Token saved successfully.")
    except Exception as e:
        print(f"Failed to save token: {e}")

def delete_token():
    try:
        win32cred.CredDelete('FinanceTr_Access_token', win32cred.CRED_TYPE_GENERIC)
        print("Token deleted successfully.")
    except Exception as e:
        print(f"Failed to delete token: {e}")

def retrieve_token():
    try:
        cred = win32cred.CredRead('FinanceTr_Access_token', win32cred.CRED_TYPE_GENERIC)
        token = cred['CredentialBlob'].decode('utf-16').rstrip('\x00')
        print("Token retrieved successfully.")
        return verify_token(token)
    except Exception as e:
        print(f"Failed to retrieve token: {e}")
        return None
