import gspread

from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

try:

    import streamlit as st

    CREDS = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=SCOPES
    )

except Exception:

    CREDS = Credentials.from_service_account_file(
        "google_credentials.json",
        scopes=SCOPES
    )

CLIENT = gspread.authorize(CREDS)

SHEET = CLIENT.open(
    "Photo Coach Analytics"
).sheet1


def log_event(event, value=""):

    from datetime import datetime

    SHEET.append_row(
        [
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            event,
            value
        ]
    )