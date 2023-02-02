from Domoblaze_Web.Page.signup_page import SignUpPage
import allure
import pytest
class Test_SignUPPage(SignUpPage):
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_signup(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName()
        signup.SignUp_Password()
        signup.SignUp_Button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_sign_up_username_number(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName_Number()
        signup.SignUp_Password()
        signup.SignUp_Button()
        signup.Switch_Alert()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_sign_up_username_empty(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName_Empty()
        signup.SignUp_Password()
        signup.SignUp_Button()
        signup.Switch_Alert()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_sign_up_password_empty(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName()
        signup.SignUp_Password_Empty()
        signup.SignUp_Button()
        signup.Switch_Alert()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_sign_up_password_letters(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName()
        signup.SignUp_Password_Letters()
        signup.SignUp_Button()
        signup.Switch_Alert()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_sign_up_emppty_username_password(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName_Empty()
        signup.SignUp_Password_Empty()
        signup.SignUp_Button()
        signup.Switch_Alert()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_sign_up_close_button(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName()
        signup.SignUp_Password()
        signup.SignUp_Close_Button()