from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
from Domoblaze_Web.Locator.Cart_locator import Cart_Locator
class CartPage(Cart_Locator):
    def _init_(self, driver):
        self.driver = driver
    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.DEMOBLAZE)
        self.driver.maximize_window()
        sleep(2)
    def Cart_link(self):
        menu = self.URL
        men = 'li'
        me = self.driver.find_element(By.XPATH, menu)
        m = me.find_elements(By.TAG_NAME, men)
        for n in m:
            if n.text == 'Cart':
                n.click()
                break
        self.driver.implicitly_wait(5)
        # self.driver.find_element(By.XPATH, self.CART).click()
        # sleep(2)
    def OrederPlace_button(self):
        self.driver.find_element(By.XPATH, self.PLACE_ORDER).click()
        sleep(2)
    def NameField(self):
        self.driver.find_element(By.XPATH, self.NAME).clear()
        self.driver.find_element(By.XPATH, self.NAME).send_keys("belay")
        sleep(2)

    def Country(self):
        self.driver.find_element(By.XPATH, self.COUNTRY).clear()
        self.driver.find_element(By.XPATH, self.COUNTRY).send_keys("beersheva")
        sleep(2)
    def City(self):
        self.driver.find_element(By.XPATH, self.CITY).clear()
        self.driver.find_element(By.XPATH, self.CITY).send_keys("beersheva")
        sleep(2)
    def CreditFard(self):
        self.driver.find_element(By.XPATH, self.CARD).clear()
        self.driver.find_element(By.XPATH, self.CARD).send_keys("cvswhjneui")
        sleep(2)
    def Month(self):
        self.driver.find_element(By.XPATH, self.MONTH).clear()
        self.driver.find_element(By.XPATH, self.MONTH).send_keys("cvejekd")
        sleep(2)
    def Year(self):
        self.driver.find_element(By.XPATH, self.YEAR).clear()
        self.driver.find_element(By.XPATH, self.YEAR).send_keys("cvswihk3iejokl")
        sleep(2)
    def Purchase_Button(self):
        self.driver.find_element(By.XPATH, self.PURCHASE).click()
        sleep(2)
    def Close(self):
        self.driver.find_element(By.XPATH, self.CLOSE).click()
        sleep(2)
    def Assert(self):
        res = self.driver.find_element(By.XPATH, self.ASSERT).text
        assert res=="OK"
        sleep(2)

    @property
    def SwitchAlert2(self):
        return self.driver.switch_to.alert.accept()
    def Delete(self):
        self.driver.find_element(By.XPATH, self)
    def NameField_Empty(self):
        self.driver.find_element(By.XPATH, self.NAME).clear()
        self.driver.find_element(By.XPATH, self.NAME).send_keys("")
        sleep(2)
    def Country_empty(self):
        self.driver.find_element(By.XPATH, self.COUNTRY).clear()
        self.driver.find_element(By.XPATH, self.COUNTRY).send_keys("")
        sleep(2)
    def City_Empty(self):
        self.driver.find_element(By.XPATH, self.CITY).clear()
        self.driver.find_element(By.XPATH, self.CITY).send_keys("")
        sleep(2)
    def CreditCard_Empty(self):
        self.driver.find_element(By.XPATH, self.CARD).clear()
        self.driver.find_element(By.XPATH, self.CARD).send_keys("")
        sleep(2)
    def Month_Empty(self):
        self.driver.find_element(By.XPATH, self.MONTH).clear()
        self.driver.find_element(By.XPATH, self.MONTH).send_keys("")
        sleep(2)
    def Year_Empty(self):
        self.driver.find_element(By.XPATH, self.YEAR).clear()
        self.driver.find_element(By.XPATH, self.YEAR).send_keys("")
        sleep(2)
    def Close_Button(self):
        self.driver.find_element(By.XPATH, self.CLOSE).click()
        sleep(2)

    @property
    def Switch_Alert(self):
        return self.driver.switch_to.alert.text


    def assert_ok(self):
        tex = self.driver.find_element(By.XPATH, "//button[contains(text(),'OK')]").text
        assert tex=='OK'

    @property
    def Switch_Alert2(self):
        return self.driver.switch_to.alert.text

