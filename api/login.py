import app
import requests
import logging


class LoginApi:

    def __init__(self):
        self.login_url = app.BASE_URL + "/api/sys/login"

    def login(self, mobile, password):
        logging.info("param mobile={} password={}".format(mobile, password))
        data = {}
        if mobile:
            data["mobile"] = mobile
        if password:
            data["password"] = password

        if data:
            return requests.post(self.login_url, json=data)
        else:
            return requests.post(self.login_url)
