import requests
from utils.urls import Urls
from utils.handle import Handle

class UserAPIRoutes:
    def post_v1_courier_create(self, data=None):
        url = f"{Urls.URL}{Handle.COURIER}"
        resp = requests.post(url, json=data)
        return resp

    def post_v1_courier_login(self, data=None):
        url = f"{Urls.URL}{Handle.LOGIN_COURIER}"
        resp = requests.post(url, json=data, headers={'Content-Type': 'application/json'})
        return resp

    def get_v1_orders(self, params=None):
        url = f"{Urls.URL}{Handle.CREATE_ORDER}"
        resp = requests.get(url, params=params)
        return resp

    def post_v1_orders(self, data=None):
        url = f"{Urls.URL}{Handle.CREATE_ORDER}"
        resp = requests.post(url, data=data, headers = {'Content-Type': 'application/json'})
        return resp