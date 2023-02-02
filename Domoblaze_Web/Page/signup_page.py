from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
from Domoblaze_Web.Locator.Signup_locator import SignUp_Locator
class SignUpPage(SignUp_Locator):

    def _init_(self, driver):
        self.driver = driver

    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.DEMOBLAZE)
        self.driver.maximize_window()
        sleep(2)
    def SignUp_link(self):
        #self.driver.find_element(By.XPATH, self.SIGNUP).click()
        menu = self.URL
        men = 'li'
        me = self.driver.find_element(By.XPATH, menu)
        m = me.find_elements(By.TAG_NAME, men)
        for n in m:
            if n.text == 'Sign up':
                n.click()
                break
        self.driver.implicitly_wait(10)
    def SignUp_UserName(self):
        self.driver.find_element(By.XPATH, self.SIGNUP_USERNAME).clear()
        self.driver.find_element(By.XPATH, self.SIGNUP_USERNAME).send_keys("belay")
        sleep(2)
    def SignUp_Password(self):
        self.driver.find_element(By.XPATH, self.SIGNUP_PASSWORD).clear()
        self.driver.find_element(By.XPATH, self.SIGNUP_PASSWORD).send_keys("1234")
        sleep(2)
    def SignUp_Button(self):
        self.driver.find_element(By.XPATH, self.SIGNUP_BUTTON).click()
        sleep(2)
    def SignUp_UserName_Empty(self):
        self.driver.find_element(By.XPATH, self.SIGNUP_USERNAME).clear()
        self.driver.find_element(By.XPATH, self.SIGNUP_USERNAME).send_keys("")
        sleep(2)
    def SignUp_Password_Empty(self):
        self.driver.find_element(By.XPATH, self.SIGNUP_PASSWORD).clear()
        self.driver.find_element(By.XPATH, self.SIGNUP_PASSWORD).send_keys("")
        sleep(2)
    def SignUp_UserName_Number(self):
        self.driver.find_element(By.XPATH, self.SIGNUP_USERNAME).clear()
        self.driver.find_element(By.XPATH, self.SIGNUP_USERNAME).send_keys("1234")
        sleep(2)
    def SignUp_Password_Letters(self):
        self.driver.find_element(By.XPATH, self.SIGNUP_PASSWORD).clear()
        self.driver.find_element(By.XPATH, self.SIGNUP_PASSWORD).send_keys("belay")
        sleep(2)
    def Switch_Alert(self):
        self.driver.switch_to.alert.accept()
        sleep(2)
    def SignUp_Close_Button(self):
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        sleep(2)