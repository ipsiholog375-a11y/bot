import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv(Path(__file__).resolve().parent / ".env")


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Environment variable {name} is not set")
    return value


BOT_TOKEN = require_env("BOT_TOKEN")
ADMIN_ID = int(require_env("ADMIN_ID"))
PAYMENT_LINK = require_env("PAYMENT_LINK")
CONTACT_LINK = require_env("CONTACT_LINK")
