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

# Constants from environment
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
LOGIN_SERVICE = os.getenv('LOGIN_SERVICE')


def verify_access_token(token):
    if not token:
        return 'Invalid'

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        exp_time = datetime.fromtimestamp(payload.get('exp'))
        if exp_time > datetime.now():
            return token
        else:
            return 'Expired'
    except JWTError:
        return 'Invalid'


def verify_refresh_token(token):
    if not token:
        return 'Invalid'

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        exp_time = datetime.fromtimestamp(payload.get('exp'))
        time_remaining = exp_time - datetime.now()
        if time_remaining.total_seconds() > 172800:  # 2 days in seconds
            return token
        else:
            return 'Expires'
    except JWTError:
        return 'Invalid'


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


def delete_token(target_name):
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
    retrieved_token = retrieve_token('FinanceTr_Access_token')
    access_token_validity = verify_access_token(retrieved_token)

    if access_token_validity != 'Invalid':
        return retrieved_token
    else:
        refresh_token = retrieve_token('FinanceTr_Refresh_token')
        refresh_token_validity = verify_refresh_token(refresh_token)

        if refresh_token_validity == 'Expires':
            new_refresh_token = refresh_token(refresh_token, 'FinanceTr_Refresh_token')
        else:
            new_refresh_token = refresh_token

        new_access_token = refresh_token(new_refresh_token, 'FinanceTr_Access_token')
        return new_access_token


def refresh_access_token(token):
    headers = {'Authorization': f'Bearer {token}'}
    new_token = requests.get(f"{LOGIN_SERVICE}/login", headers=headers)

    save_token(new_token, 'FinanceTr_Access_token')
    return new_token


def refresh_refresh_token(token):
    headers = {'Authorization': f'Bearer {token}'}
    new_token = requests.get(f"{LOGIN_SERVICE}/login", headers=headers)

    save_token(new_token, 'FinanceTr_Refresh_token')
    return new_token
