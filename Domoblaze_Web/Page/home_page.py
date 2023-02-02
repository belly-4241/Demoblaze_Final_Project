from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
from Domoblaze_Web.Locator.home_locator import Home_Locator
class HomePage(Home_Locator):

    def _init_(self, driver):
        self.driver = driver

    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.DEMOBLAZE)
        self.driver.maximize_window()
        sleep(2)
    def homeLink(self):
        menu = self.URL
        men = 'li'
        me = self.driver.find_element(By.XPATH, menu)
        m = me.find_elements(By.TAG_NAME, men)
        for n in m:
            if n.text == 'Home':
                n.click()
                break
        self.driver.implicitly_wait(10)
        # self.driver.find_element(By.XPATH, self.HOME).click()
        # sleep(2)
    def Phone_categories(self):
        self.driver.find_element(By.XPATH, self.PHONE).click()
        sleep(2)
    def Laptop(self):
        self.driver.find_element(By.XPATH, self.LAPTOP).click()
        sleep(2)
    def Monitor(self):
        self.driver.find_element(By.XPATH, self.MONITOR).click()
        sleep(2)
    def Samsung_galaxys7(self):
        self.driver.find_element(By.XPATH, self.SUMSUNG_GALAXY_S6).click()
        sleep(2)
    def back(self):
        self.driver.find_element(By.XPATH, self.BACK)
        sleep(3)
    def sony_galaxy(self):
        self.driver.find_element(By.XPATH, self.SONY_XPERIAL).click()
        sleep(2)
    def sumsung_galaxy(self):
        self.driver.find_element(By.XPATH, self.SUMSUNG_GALAXY).click()
        sleep(2)
    def Laptop_Macbook_Air(self):
        self.driver.find_element(By.XPATH, self.MACBOOK_AIR).click()
        sleep(2)
    def Monitor_Asus_Full_HD(self):
        self.driver.find_element(By.XPATH, self.ASUS_FULL_HD).click()
        sleep(2)
    def AddTocart(self):
        self.driver.find_element(By.XPATH, self.ADDTO_CART).click()
        sleep(2)
    def SwitchAlert(self):
        self.driver.switch_to.alert.accept()
        sleep(2)
    def Cart(self):
        self.driver.find_element(By.XPATH, self.CART).click()
        sleep(2)
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

    def test_HomeLeftSide_button(self):
        self.driver.find_element(By.XPATH, self.LEFT_SIDE_BUTTON).click()
        sleep(2)
    def test_HomeRightSide_button(self):
        self.driver.find_element(By.XPATH, self.RIGHT_SIDE_BUTTON).click()
        sleep(2)
    def test_Home_Next_Button(self):
        self.driver.find_element(By.XPATH, self.NEXT_BUTTON).click()
        sleep(2)
    def test_Home_Previous_Button(self):
        self.driver.find_element(By.XPATH, self.PREVIOUS_BUTTON).click()
        sleep(2)