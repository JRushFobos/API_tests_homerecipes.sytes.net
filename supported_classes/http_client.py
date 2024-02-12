import os
import json
import requests

from dotenv import load_dotenv

load_dotenv()


class CustomHttpClient:
    def __init__(self):
        self.site = "https://homerecipes.sytes.net"
        self.headers =  {
            "Content-Type": "application/json",
            "accept": "application/json;charset=utf-8",
        }
        self.enable_admin_authorization()

    def set_headers(self, new_dict):
        self.headers = new_dict
        return self

    def enable_admin_authorization(self):
        url = "https://homerecipes.sytes.net//api/auth/token/login/"
        body = {"email": os.getenv("LOGIN"),
                "password": os.getenv("PASSWORD")}
        request = requests.post(url, data=body)
        token = request.json()["auth_token"]
        self.headers["Authorization"] = f"Token {token}"
        return self

    def disable_authorization(self):
        del self.headers["Authorization"]
        return self

    def get(self, path):
        return requests.get(f"{self.site}/{path}", headers=self.headers)

    def post(self, path, data=None, files=None):
        if files is not None:
            return requests.post(
                f"{self.site}/{path}",
                headers=self.headers,
                files=files,
            )
        else:
            return requests.post(
                f"{self.site}/{path}",
                headers=self.headers,
                data=json.dumps(data),
                files=files,
            )

    def put(self, path, data=None, files=None):
        if files is None:
            return requests.put(f"{self.site}/{path}",
                                 headers=self.headers,
                                 data=json.dumps(data))
        else:
            return requests.put(f"{self.site}/{path}",
                                 headers=self.headers,
                                 data=json.dumps(data),files=files)

    def delete(self, path):
        return requests.delete(f"{self.site}/{path}", headers=self.headers)
