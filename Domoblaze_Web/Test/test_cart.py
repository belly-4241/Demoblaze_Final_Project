from Domoblaze_Web.Page.cart_page import CartPage
import allure
import pytest
class Test_Cart(CartPage):
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField()
        cart.Country()
        cart.City()
        cart.CreditFard()
        cart.Month()
        cart.Year()
        cart.Purchase_Button()
        cart.assert_ok()


    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_name_empty(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField_Empty()
        cart.Country()
        cart.City()
        cart.CreditFard()
        cart.Month()
        cart.Year()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Name and Creditcard." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_empty_country(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField()
        cart.Country_empty()
        cart.City()
        cart.CreditFard()
        cart.Month()
        cart.Year()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Usern Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_empty_city(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField()
        cart.Country()
        cart.City_Empty()
        cart.CreditFard()
        cart.Month()
        cart.Year()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Userd Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_empty_creditcard(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField()
        cart.Country()
        cart.City()
        cart.CreditCard_Empty()
        cart.Month()
        cart.Year()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Userand Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_empty_month(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField()
        cart.Country()
        cart.City()
        cart.CreditFard()
        cart.Month_Empty()
        cart.Year()
        cart.Purchase_Button()
        cart.assert_ok()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_empty_year(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField()
        cart.Country()
        cart.City()
        cart.CreditFard()
        cart.Month()
        cart.Year_Empty()
        cart.Purchase_Button()
        cart.assert_ok()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_close_button(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField()
        cart.Country()
        cart.City()
        cart.CreditFard()
        cart.Month()
        cart.Year()
        cart.Close_Button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_name_country_empty(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField_Empty()
        cart.Country_empty()
        cart.City()
        cart.CreditFard()
        cart.Month()
        cart.Year()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Username and Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_name_city_empty(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField_Empty()
        cart.Country()
        cart.City_Empty()
        cart.CreditFard()
        cart.Month()
        cart.Year()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Username and Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_name_creditcard_empty(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField_Empty()
        cart.Country()
        cart.City()
        cart.CreditCard_Empty()
        cart.Month()
        cart.Year()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Username and Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_name_month_empty(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField_Empty()
        cart.Country()
        cart.City()
        cart.CreditFard()
        cart.Month_Empty()
        cart.Year()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Username and Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_name_year_empty(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField_Empty()
        cart.Country()
        cart.City()
        cart.CreditFard()
        cart.Month()
        cart.Year_Empty()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Username and Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_country_city_empty(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField()
        cart.Country_empty()
        cart.City_Empty()
        cart.CreditFard()
        cart.Month()
        cart.Year()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Username and Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_country_creditcard_empty(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField()
        cart.Country_empty()
        cart.City()
        cart.CreditCard_Empty()
        cart.Month()
        cart.Year()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Username and Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_country_month_empty(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField()
        cart.Country_empty()
        cart.City()
        cart.CreditFard()
        cart.Month_Empty()
        cart.Year()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Username and Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_country_year_empty(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField()
        cart.Country_empty()
        cart.City()
        cart.CreditFard()
        cart.Month()
        cart.Year_Empty()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Name and Creditcard." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_city_creditcard_empty(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField()
        cart.Country()
        cart.City_Empty()
        cart.CreditCard_Empty()
        cart.Month()
        cart.Year()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Name and Creditcard." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_city_month_empty(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField()
        cart.Country()
        cart.City_Empty()
        cart.CreditFard()
        cart.Month_Empty()
        cart.Year()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Username and Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_city_year_empty(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField()
        cart.Country()
        cart.City_Empty()
        cart.CreditFard()
        cart.Month()
        cart.Year_Empty()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Username and Password." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_creditcard_month_empty(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField()
        cart.Country()
        cart.City()
        cart.CreditCard_Empty()
        cart.Month_Empty()
        cart.Year()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Name and Creditcard." == CHECK

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_cart_creditcard_year_empty(self):
        cart = CartPage()
        cart.open()
        cart.Cart_link()
        cart.OrederPlace_button()
        cart.NameField()
        cart.Country()
        cart.City()
        cart.CreditCard_Empty()
        cart.Month()
        cart.Year_Empty()
        cart.Purchase_Button()
        CHECK = cart.Switch_Alert
        assert "Please fill out Name and Creditcard." == CHECK
