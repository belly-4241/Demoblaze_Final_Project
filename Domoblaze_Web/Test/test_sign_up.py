from Domoblaze_Web.Page.signup_page import SignUpPage
import allure
import pytest
class Test_SignUPPage(SignUpPage):
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_signup_letter_username_password(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName_number()
        signup.SignUp_Password_number()
        signup.SignUp_Button()
        CHECK = signup.Switch_Alert
        assert "This user already exist." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_sign_up_number_username_password(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName_letters()
        signup.SignUp_Password_letters()
        signup.SignUp_Button()
        CHECK = signup.Switch_Alert
        assert "Please fill out Username and Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_sign_up_letters_username_num_pass(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName_letters()
        signup.SignUp_Password_number()
        signup.SignUp_Button()
        CHECK = signup.Switch_Alert
        assert "This user already exist." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_sign_up_letters_password_number_user(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName_number()
        signup.SignUp_Password_letters()
        signup.SignUp_Button()
        CHECK = signup.Switch_Alert
        assert "Please fill out Username and Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_sign_up_empty_password_letters_user(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName_empty()
        signup.SignUp_Password_letters()
        signup.SignUp_Button()
        CHECK = signup.Switch_Alert
        assert "Please fill out Username and Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_sign_up_numbers_username_empty_password(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName_empty()
        signup.SignUp_Password_number()
        signup.SignUp_Button()
        CHECK = signup.Switch_Alert
        assert "Please fill out Username and Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_sign_up_empty_user_letters_pass(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName_number()
        signup.SignUp_Password_empty()
        CHECK = signup.Switch_Alert
        assert "This user already exist." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_sign_up_empty_user_num_pass(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName_number()
        signup.SignUp_Password_empty()
        signup.SignUp_Button()
        CHECK = signup.Switch_Alert
        assert "This user already exist." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_sign_up_empty_user_empty_pass(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName_empty()
        signup.SignUp_Password_empty()
        signup.SignUp_Button()
        CHECK = signup.Switch_Alert
        assert "This user already exist." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_sign_up_exist_account(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName_exit()
        signup.SignUp_Password_exit()
        signup.SignUp_Button()
        CHECK = signup.Switch_Alert
        assert "This user already exist." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_sign_up_close_button(self):
        signup = SignUpPage()
        signup.open()
        signup.SignUp_link()
        signup.SignUp_UserName_exit()
        signup.SignUp_Password_exit()
        signup.SignUp_Close_Button()
