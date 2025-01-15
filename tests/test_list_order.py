import json
import allure
from utils.routes import UserAPIRoutes

class TestListOrder:
    @allure.title('В тело ответа возвращается список заказов')
    def test_response_contains_list_of_order(self):
        params= {
            'nearestStation': json.dumps(['1', '2'])
        }
        response = UserAPIRoutes().get_v1_orders(params=params)
        assert response.status_code == 200 and "orders" in response.json()