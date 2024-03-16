import os


class Config:

    BOT_TOKEN = 6446514676:AAEvI-WBqoNy_B43QwNm1V6oIrq8oizmdk0

    SESSION_NAME = kawinraju

    API_ID = 11394583

    API_HASH = d251275f6bcd8dc44c59b2fd99d1552b

    CLIENT_ID = 139072163307-dis5shj3ph2g2aq20r37i5ftnujdhsvc.apps.googleusercontent.com

    CLIENT_SECRET = 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

    BOT_OWNER = 5968064176

    AUTH_USERS_TEXT = 6095233308

    AUTH_USERS = [BOT_OWNER, 6095233308] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
    
