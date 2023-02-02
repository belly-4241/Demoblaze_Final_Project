from Domoblaze_Web.Page.about_us_page import About_Us_Locator, AboutTest
import allure
import pytest
class Test_Link(About_Us_Locator):
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_about(self):
        about_us = AboutTest()
        about_us.open()
        about_us.About_Us_link()
        about_us.Play_Button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_about_timer_check(self):
        about_us = AboutTest()
        about_us.open()
        about_us.About_Us_link()
        about_us.Play_Button()
        about_us.Timer_Check()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_about_close_button(self):
        about_us = AboutTest()
        about_us.open()
        about_us.About_Us_link()
        about_us.Close_Button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_about_ckeck_speaker(self):
        about_us = AboutTest()
        about_us.open()
        about_us.About_Us_link()
        about_us.Play_Button()
        about_us.Check_Speaker()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_about_zoom_button(self):
        about_us = AboutTest()
        about_us.open()
        about_us.About_Us_link()
        about_us.Play_Button()
        about_us.Zoom_Button_Check()
