import allure
import pytest
from utils.data import User
from utils.routes import UserAPIRoutes

class TestLoginCourier:

    @allure.title('Авторизация курьера с валидными данными возвращает id')
    @allure.description('Логинимся с валидными данными, проверяем что запрос возвращает id')
    def test_login_courier_positive_result(self, login_and_del_user):
        response = UserAPIRoutes().post_v1_courier_login(data=login_and_del_user)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Ошибка авторизации, если логин или пароль некорректные')
    @allure.description('Логинимся с невалидными данными, проверяем что запрос возвращает соответствующую ошибку')
    def test_login_courier_not_found_return_error(self):
        response = UserAPIRoutes().post_v1_courier_login(data=User.data_incorrect)
        assert response.status_code == 404 and 'Учетная запись не найдена' in response.text

    @allure.title('Ошибка авторизации, если поле логин или пароль пустое')
    @allure.description('Логинимся с незаполненным полем логин или пароль, \
    проверяем что запрос возвращает соответствующую ошибку')
    @pytest.mark.parametrize('data_without_login_or_password', [User.data_without_login, User.data_without_password])
    def test_login_courier_not_all_data_return_error(self, data_without_login_or_password):
        response = UserAPIRoutes().post_v1_courier_login(data=data_without_login_or_password)
        assert response.status_code == 400 and 'Недостаточно данных для входа' in response.text