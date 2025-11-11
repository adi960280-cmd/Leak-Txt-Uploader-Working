# config.py
import os

# Bot Configuration
BOT_NAME = os.environ.get('BOT_NAME', 'ZENITH_BOT')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '7662019980:AAGQnhhOhWxi69j3aWTFfOCUNQhbgtxSz9M')
API_ID = int(os.environ.get('API_ID', '29115102'))
API_HASH = os.environ.get('API_HASH', '1a331db2b00e9d2decaa9c7276449eb6')
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb+srv://herukobanna:ankit999@cluster0.xs772me.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

# Additional Configuration
OWNER_ID = int(os.environ.get('OWNER_ID', '1224092270'))
LOG_CHANNEL_ID = int(os.environ.get('LOG_CHANNEL_ID', '-1002067304488'))

