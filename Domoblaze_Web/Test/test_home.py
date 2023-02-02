import pytest

from Domoblaze_Web.Page.home_page import HomePage
import allure
@allure.severity(allure.severity_level.NORMAL)
class Test_Home(HomePage):
    @allure.step
    @allure.description("")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_home_phone(self):
        homepage = HomePage()
        homepage.open()
        homepage.homeLink()
        homepage.Phone_categories()
        homepage.Samsung_galaxys7()
        homepage.AddTocart()
        homepage.SwitchAlert()
        homepage.driver.back()
        homepage.driver.back()
        homepage.sony_galaxy()
        homepage.AddTocart()
        homepage.SwitchAlert()
        homepage.driver.back()
        homepage.driver.back()
        homepage.sumsung_galaxy()
        homepage.AddTocart()
        homepage.SwitchAlert()
        homepage.Cart()
        homepage.OrederPlace_button()
        homepage.NameField()
        #HomePage.Country()
        homepage.City()
        homepage.CreditFard()
        homepage.Month()
        homepage.Year()
        homepage.Purchase_Button()
        homepage.Assert()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_home_laptop(self):
        homepage = HomePage()
        homepage.open()
        homepage.homeLink()
        homepage.Laptop()
        homepage.Laptop_Macbook_Air()
        homepage.AddTocart()
        homepage.SwitchAlert()
        homepage.Cart()
        homepage.OrederPlace_button()
        homepage.NameField()
        # HomePage.Country()
        homepage.City()
        homepage.CreditFard()
        homepage.Month()
        homepage.Year()
        homepage.Purchase_Button()
        homepage.Assert()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_home_monitor(self):
        homepage = HomePage()
        homepage.open()
        homepage.homeLink()
        homepage.Monitor()
        homepage.Monitor_Asus_Full_HD()
        homepage.AddTocart()
        homepage.SwitchAlert()
        homepage.Cart()
        homepage.OrederPlace_button()
        homepage.NameField()
        # HomePage.Country()
        homepage.City()
        homepage.CreditFard()
        homepage.Month()
        homepage.Year()
        homepage.Purchase_Button()
        homepage.Assert()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_HomeLeftSide_button(self):
        homepage = HomePage()
        homepage.open()
        homepage.homeLink()
        homepage.test_HomeLeftSide_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_HomeRightSide_button(self):
        homepage = HomePage()
        homepage.open()
        homepage.homeLink()
        homepage.test_HomeRightSide_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_Home_Next_Button(self):
        homepage = HomePage()
        homepage.open()
        homepage.homeLink()
        homepage.test_Home_Next_Button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_Home_Previous_Button(self):
        homepage = HomePage()
        homepage.open()
        homepage.homeLink()
        homepage.test_Home_Previous_Button()


