#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "20168440"))
API_HASH = environ.get("API_HASH", "903ed715faf0c0729d9c5f221a6f2bc1")
BOT_TOKEN = environ.get("7794809702:AAGGU0JIg5NIXXoapyyT_albAuuj69PpoQk")
OWNER = int(environ.get("OWNER", "6027045449"))
CREDIT = environ.get("CREDIT", "Venom") 
TOTAL_USER = os.environ.get('TOTAL_USERS','6027045449' ).split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]
AUTH_USER = os.environ.get('AUTH_USERS', '6027045449').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

