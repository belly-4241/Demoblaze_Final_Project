from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
from Domoblaze_Web.Locator.contact_locator import Contact_Locator
class Contact(Contact_Locator):

    def _init_(self, driver):
        self.driver = driver

    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.DEMOBLAZE)
        self.driver.maximize_window()
        sleep(2)

    def Contact_Link(self):
        menu = self.URL
        men = 'li'
        me = self.driver.find_element(By.XPATH, menu)
        m = me.find_elements(By.TAG_NAME, men)
        for n in m:
            if n.text == 'Contact':
                n.click()
                break
        self.driver.implicitly_wait(10)
        # self.driver.find_element(By.XPATH, self.CONTACT).click()
        # sleep(2)
    def Contact_Email(self):
        self.driver.find_element(By.XPATH, self.EMAIL).clear()
        self.driver.find_element(By.XPATH, self.EMAIL).send_keys("bell")
        sleep(2)
    def Contact_Name(self):
        self.driver.find_element(By.XPATH, self.NAME).clear()
        self.driver.find_element(By.XPATH, self.NAME).send_keys("belly")
        sleep(2)
    def Contact_Message(self):
        self.driver.find_element(By.XPATH, self.MESSAGE).clear()
        self.driver.find_element(By.XPATH, self.MESSAGE).send_keys("I wanna be your stafmate")
        sleep(2)
    def Send_Button(self):
        self.driver.find_element(By.XPATH, self.SEND_BUTTON).click()
        sleep(2)
    def Switch_Alert(self):
        self.driver.switch_to.alert.accept()
        sleep(2)
    def Contact_Invalid_Name(self):
        self.driver.find_element(By.XPATH, self.NAME).clear()
        self.driver.find_element(By.XPATH, self.NAME).send_keys("12234")
        sleep(2)
    def Contact_Invalid_Email(self):
        self.driver.find_element(By.XPATH, self.EMAIL).clear()
        self.driver.find_element(By.XPATH, self.EMAIL).send_keys("12234")
        sleep(2)
    def Contact_Empty_Message(self):
        self.driver.find_element(By.XPATH, self.MESSAGE).clear()
        self.driver.find_element(By.XPATH, self.MESSAGE).send_keys("")
        sleep(2)
    def Contact_Empty_Email(self):
        self.driver.find_element(By.XPATH, self.EMAIL).clear()
        self.driver.find_element(By.XPATH, self.EMAIL).send_keys("")
        sleep(2)
    def Contact_Empty_Name(self):
        self.driver.find_element(By.XPATH, self.NAME).clear()
        self.driver.find_element(By.XPATH, self.NAME).send_keys("")
        sleep(2)
    def Contact_Close_Button(self):
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        sleep(2)

