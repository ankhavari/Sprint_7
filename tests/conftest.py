import pytest
import requests
from utils.routes import UserAPIRoutes
from utils.handle import Handle
from utils.urls import Urls
from utils.user_generator import register_new_courier_and_return_login_password as reg
from utils.user_generator import generating_user_data as gen

@pytest.fixture(scope='function')
def login_and_del_user():
    login_pass = reg()
    resp = UserAPIRoutes().post_v1_courier_login(data=login_pass)
    id_courier = resp.json()['id']
    yield login_pass
    payload ={
        "id": id_courier,
    }
    requests.delete(f'{Urls.URL}{Handle.COURIER}{id_courier}', json=payload)

@pytest.fixture(scope='function')
def prepare_and_del_courier():
    login_pass = gen()
    yield login_pass
    resp = requests.post(f'{Urls.URL}{Handle.LOGIN_COURIER}', json=login_pass)
    id_courier = resp.json()['id']
    payload ={
        "id": id_courier,
    }
    requests.delete(f'{Urls.URL}{Handle.COURIER}', json=payload)