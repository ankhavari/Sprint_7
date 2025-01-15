import requests
import random
import string
from faker import Faker

# метод регистрации нового курьера возвращает словарь из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём словарь, чтобы метод мог его вернуть
    login_pass = {}

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в словарь логин и пароль курьера
    if response.status_code == 201:
        login_pass['login'] = login
        login_pass['password'] = password

    # возвращаем словарь
    return login_pass

# метод возвращает словарь со сгенерированными данными для логина, пароля и фамилии
def generating_user_data():
    fake = Faker()
    login = fake.user_name()
    password = fake.password()
    first_name = fake.first_name()
    reg_data = {"login": login, "password": password, "firstName": first_name}
    return reg_data

# метод возвращает словарь со сгенерированными данными для пароля и фамилии
def generating_user_data_without_login():
    fake = Faker()
    password = fake.password()
    first_name = fake.first_name()
    reg_data = {"password": password, "firstName": first_name}
    return reg_data

# метод возвращает словарь со сгенерированными данными для логина и фамилии
def generating_user_data_without_password():
    fake = Faker()
    login = fake.user_name()
    first_name = fake.first_name()
    reg_data = {"login": login, "firstName": first_name}
    return reg_data