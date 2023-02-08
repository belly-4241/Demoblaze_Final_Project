from Domoblaze_Web.Page.login_page import LoginPage
import allure
import pytest
class Test_Login(LoginPage):
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_login_valid(self):
        login = LoginPage()
        login.open()
        login.Login_link()
        login.Login_Username()
        login.Login_Password()
        login.Login_Button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity

    @allure.step
    @allure.description("")
    def test_login_username_empty(self):
        login = LoginPage()
        login.open()
        login.Login_link()
        login.Username_Empty()
        login.Login_Password()
        login.Login_Button()
        CHECK = login.Switch_Alert
        assert "Please fill out Username and Password."==CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_login_password_empty(self):
        login = LoginPage()
        login.open()
        login.Login_link()
        login.Login_Username()
        login.Password_Empty()
        login.Login_Button()
        CHECK = login.Switch_Alert
        assert "Please fill out Username and Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_login_invalid_username(self):
        login = LoginPage()
        login.open()
        login.Login_link()
        login.UserName_Number()
        login.Login_Password()
        login.Login_Button()
        CHECK = login.Switch_Alert
        assert 'Wrong password.' == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_login_invalid_password(self):
        login = LoginPage()
        login.open()
        login.Login_link()
        login.Login_Username()
        login.Password_Number()
        login.Login_Button()
        CHECK = login.Switch_Alert
        assert 'Please fill out Username and Password.' == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_login_username_password_number(self):
        login = LoginPage()
        login.open()
        login.Login_link()
        login.UserName_Number()
        login.Password_Number()
        login.Login_Button()
        CHECK = login.Switch_Alert
        assert 'Please fill out Username and Password.' == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_login_close_button(self):
        login = LoginPage()
        login.open()
        login.Login_link()
        login.Login_Username()
        login.Login_Password()
        login.Close_Button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_login_link(self):
        login = LoginPage()
        login.open()
        login.Login_link()
        login.Username_Empty()
        login.Password_Empty()
        login.Login_Button()
    def test_login_empty_password_invalid_username(self):
        login = LoginPage()
        login.open()
        login.Login_link()
        login.UserName_Number()
        login.Password_Empty()
        login.Login_Button()
        CHECK = login.Switch_Alert
        assert 'Please fill out Username and Password.' == CHECK
    def test_login_invalid_password_empty_username(self):
        login = LoginPage()
        login.open()
        login.Login_link()
        login.Username_Empty()
        login.Password_Number()
        login.Login_Button()
        CHECK = login.Switch_Alert
        assert 'Please fill out Username and Password.' == CHECK
