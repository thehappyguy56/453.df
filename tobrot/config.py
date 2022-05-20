import os


class Config((object)):
    # get a token from @BotFather
    TG_BOT_TOKEN = "5345031636:AAHOn40snmudVO-xX7s8OKN4QPYvp3xy_ZI"
    # The Telegram API things
    APP_ID = 11647359
    API_HASH = "9ddec3691b4d1eb152f317887055a989"
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = -768173989
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = 128
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = "https://placehold.it/90x90"
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = 6800
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = 600
    MAX_TG_SPLIT_FILE_SIZE = 1072864000
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = "█"
    UN_FINISHED_PROGRESS_STR = "░"
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "")
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", "")
    DESTINATION_FOLDER = os.environ.get(
        "DESTINATION_FOLDER", "TorrentLeech-Gdrive")
    INDEX_LINK = "https://drive1.adib.workers.dev/0:"
