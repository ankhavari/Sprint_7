import allure
from utils.routes import UserAPIRoutes
from utils.user_generator import generating_user_data_without_password as reg_without_password
from utils.user_generator import generating_user_data_without_login as reg_without_login

class TestCreateCourier:

    @allure.title('Создание курьера с валидными данными')
    @allure.description('Создаем курьера с валидными данными, запрос возвращает правильный код и текст ответа')
    def test_create_courier_positive_result(self, prepare_and_del_courier):
        response_body = '{"ok":true}'
        response = UserAPIRoutes().post_v1_courier_create(data=prepare_and_del_courier)
        assert response.status_code == 201 and response_body == response.text

    @allure.title('Нельзя создать двух одинаковых курьеров')
    @allure.description('При попытке создать курьера с данными, которые уже есть в системе, \
    возвращается соответствующая ошибка')
    def test_request_with_duplicate_login_return_error(self, login_and_del_user):
        response = UserAPIRoutes().post_v1_courier_create(data=login_and_del_user)
        assert response.status_code == 409 and 'Этот логин уже используется' in response.text

    @allure.title('Нельзя создать курьера, не заполнив поле Пароль')
    @allure.description('При попытке создать курьера, не заполнив поле Пароль, возвращается соответствующая ошибка')
    def test_create_courier_without_password_return_error(self):
        response = UserAPIRoutes().post_v1_courier_create(data=reg_without_password())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text

    @allure.title('Нельзя создать курьера, не заполнив поле Логин')
    @allure.description('При попытке создать курьера, не заполнив поле Логин, возвращается соответствующая ошибка')
    def test_create_courier_without_login_return_error(self):
        response = UserAPIRoutes().post_v1_courier_create(data=reg_without_login())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text