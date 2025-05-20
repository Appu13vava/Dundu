# tg_bot/config.py

from tg_bot.sample_config import Config as BaseConfig

class Development(BaseConfig):
    # REQUIRED
    API_KEY = "your_actual_api_key"
    OWNER_ID = 123456789  # Replace with your Telegram user ID
    OWNER_USERNAME = "your_username"  # Replace with your Telegram @username

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "sqlite:///mydb.db"  # Or use a remote DB URI
    MESSAGE_DUMP = None
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = [123456789]  # List of Telegram user IDs
    SUPPORT_USERS = []
    WHITELIST_USERS = []
    DONATION_LINK = None
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False
    STRICT_GBAN = False
    WORKERS = 8
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'
    ALLOW_EXCL = False
    BMERNU_SCUT_SRELFTI = 0
