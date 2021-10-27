import os

from google.auth.transport import requests
from google.oauth2 import id_token

CLIENT_ID = os.getenv("CLIENT_ID")


def user_id_get(jwt_token: str) -> str:
    try:
        id_info = id_token.verify_oauth2_token(jwt_token, requests.Request(), CLIENT_ID)

        user_id = id_info['sub']
    except ValueError:
        # SampleUserのidを仮入れ
        user_id = "aiueo"

    return user_id
