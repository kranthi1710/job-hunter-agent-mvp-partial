from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    """
    Central configuration for the application.
    """

    APP_NAME = os.getenv(
        "APP_NAME",
        "Job Intelligence Platform"
    )

    REMOTEOK_URL = os.getenv(
        "REMOTEOK_URL",
        "https://remoteok.com/api"
    )

    REQUEST_TIMEOUT = int(
        os.getenv(
            "REQUEST_TIMEOUT",
            "20"
        )
    )

    EXPORT_DIRECTORY = Path(
        os.getenv(
            "EXPORT_DIRECTORY",
            "reports"
        )
    )

    DEFAULT_EXPORT_FILENAME = os.getenv(
        "DEFAULT_EXPORT_FILENAME",
        "jobs.xlsx"
    )