from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
from Domoblaze_Web.Locator.login_locator import Login_Locator
class LoginPage(Login_Locator):

    def _init_(self, driver):
        self.driver = driver

    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.DEMOBLAZE)
        self.driver.maximize_window()
        sleep(2)
    def Login_link(self):
        menu = self.URL
        men = 'li'
        me = self.driver.find_element(By.XPATH, menu)
        m = me.find_elements(By.TAG_NAME, men)
        for n in m:
            if n.text == 'Log in':
                n.click()
                break
        self.driver.implicitly_wait(10)
        # menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
        # self.driver.find_element(By.XPATH, self.LOGIN).click()
    def Login_Username(self):
        self.driver.find_element(By.XPATH, self.LOGIN_USERNAME).clear()
        self.driver.find_element(By.XPATH, self.LOGIN_USERNAME).send_keys("belay")
        sleep(2)
    def Login_Password(self):
        self.driver.find_element(By.XPATH, self.LOGIN_PASSWORD).clear()
        self.driver.find_element(By.XPATH, self.LOGIN_PASSWORD).send_keys("belay")
        sleep(2)
    def Login_Button(self):
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()
        sleep(2)
    def Close_Button(self):
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        sleep(2)
    def Username_Empty(self):
        self.driver.find_element(By.XPATH, self.LOGIN_USERNAME).clear()
        self.driver.find_element(By.XPATH, self.LOGIN_USERNAME).send_keys("")
        sleep(2)
    def Password_Empty(self):
        self.driver.find_element(By.XPATH, self.LOGIN_PASSWORD).clear()
        self.driver.find_element(By.XPATH, self.LOGIN_PASSWORD).send_keys("")
        sleep(2)
    def UserName_Number(self):
        self.driver.find_element(By.XPATH, self.LOGIN_USERNAME).clear()
        self.driver.find_element(By.XPATH, self.LOGIN_USERNAME).send_keys("1234")
        sleep(2)
    def Password_Number(self):
        self.driver.find_element(By.XPATH, self.LOGIN_USERNAME).clear()
        self.driver.find_element(By.XPATH, self.LOGIN_USERNAME).send_keys("12345")
        sleep(2)
    def Switch_Alert(self):
        self.driver.switch_to.alert.accept()
        sleep(2)
    def Log_Out(self):
        self.driver.find_element(By.XPATH, self.LOGOUT).click()
        sleep(2)