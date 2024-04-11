import os
import json
import firebase_admin
from firebase_admin import credentials
import pyrebase 

# Get environment variables from the system environment
firebase_service_account_key_str = os.environ.get('FIREBASE_SERVICE_ACCOUNT_KEY')
firebase_config_str = os.environ.get('FIREBASE_CONFIG')

# Make sure to check if the environment variables were actually retrieved
if not firebase_service_account_key_str or not firebase_config_str:
    raise ValueError("The necessary environment variables were not found.")

# Parse the service account key and firebase config from the environment variable strings
cred_dict = json.loads(firebase_service_account_key_str)
firebase_config_dict = json.loads(firebase_config_str)

# Initialize Firebase Admin with the service account information
cred = credentials.Certificate(cred_dict)
firebase_admin.initialize_app(cred)

# Initialize Pyrebase with the config information
firebase = pyrebase.initialize_app(firebase_config_dict)
db = firebase.database()
authSession = firebase.auth()
