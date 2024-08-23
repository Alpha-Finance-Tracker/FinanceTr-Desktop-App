import os
import win32cred
import requests
from dotenv import load_dotenv
from jose import jwt, JWTError
from datetime import datetime, timedelta
import logging


load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

LOGIN_SERVICE='http://127.0.0.1:8000'
FINANCE_TR_SERVICE='http://127.0.0.1:8001'


def save_token(token, target_name):
    cred = {
        'Type': win32cred.CRED_TYPE_GENERIC,
        'TargetName': target_name,
        'CredentialBlob': token,
        'Persist': win32cred.CRED_PERSIST_LOCAL_MACHINE
    }
    try:
        win32cred.CredWrite(cred, 0)
        logger.info(f"Token '{target_name}' saved successfully.")
    except Exception as e:
        logger.error(f"Failed to save token '{target_name}': {e}")


async def delete_token(target_name):
    try:
        win32cred.CredDelete(target_name, win32cred.CRED_TYPE_GENERIC)
        logger.info(f"Token '{target_name}' deleted successfully.")
    except Exception as e:
        logger.error(f"Failed to delete token '{target_name}': {e}")


def retrieve_token(target_name):
    try:
        cred = win32cred.CredRead(target_name, win32cred.CRED_TYPE_GENERIC)
        token = cred['CredentialBlob'].decode('utf-16').rstrip('\x00')
        logger.info(f"Token '{target_name}' retrieved successfully.")
        return token
    except Exception as e:
        logger.error(f"Failed to retrieve token '{target_name}': {e}")
        return None


def prepare_token_for_request():
    access_token = retrieve_token('FinanceTr_Access_token')
    verification_response = requests.get(f"{LOGIN_SERVICE}/verify_access_token",headers={'Authorization': f'Bearer {access_token}'})

    if verification_response.status_code == 200:
        return access_token

    else:
        refresh_token = retrieve_token('FinanceTr_Refresh_token')

        access_token_response =  requests.get(f"{LOGIN_SERVICE}/refresh_access_token",headers={'Authorization': f'Bearer {refresh_token}'})
        new_access_token = access_token_response.json()['token']

        if access_token_response.json()['Validity'] != 'Expires':
            save_token(new_access_token,'FinanceTr_Access_token')
            return new_access_token
        else:
            refresh_token_response = requests.get(f"{LOGIN_SERVICE}/refresh_refresh_token",headers={'Authorization': f'Bearer {refresh_token}'})
            refresh_token = refresh_token_response.json()
            save_token(refresh_token, 'FinanceTr_Refresh_token')
            return new_access_token

def check_if_login_is_needed():
    refresh_token = retrieve_token('FinanceTr_Refresh_token')
    response =  requests.get(f"{LOGIN_SERVICE}/verify_refresh_token",headers={'Authorization': f'Bearer {refresh_token}'})
    if response.json()['Validity'] == 'Valid':
        return False
