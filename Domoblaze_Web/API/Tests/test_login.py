from Domoblaze_Web.API.Locators.signup_locators import sign_up_API
import requests
import allure
@allure.description('Login correctly')
class Test_Lgin(sign_up_API):
    def test_login_correctly(self):
        url = sign_up_API.url_sign_up
        data = sign_up_API.data_valid
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    def test_login_incorrect_username(self):
        url = sign_up_API.url_sign_up
        data = sign_up_API.data_invalid_password
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    def test_login_incorrect_password(self):
        url = sign_up_API.url_sign_up
        data = sign_up_API.data_invalid_email
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    def test_login_incorrect_username_email(self):
        url = sign_up_API.url_sign_up
        data = sign_up_API.data_invalid_password_and_email
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    def test_login_empty_username(self):
        url = sign_up_API.url_sign_up
        data = sign_up_API.data_empty_UserName
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    def test_login_empty_password(self):
        url = sign_up_API.url_sign_up
        data = sign_up_API.data_empty_password
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    def test_login_empty_username_email(self):
        url = sign_up_API.url_sign_up
        data = sign_up_API.data_empty_username_password
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10