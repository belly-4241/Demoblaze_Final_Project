from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
from Domoblaze_Web.Locator.About_us_locator import About_Us_Locator
class AboutTest(About_Us_Locator):

    def _init_(self, driver):
        self.driver = driver

    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.DEMOBLAZE)
        self.driver.maximize_window()
        sleep(2)
    def About_Us_link(self):
        #self.driver.find_element(By.XPATH, self.ABOUT_US_LINK).click()
        menu = self.URL
        men = 'li'
        me = self.driver.find_element(By.XPATH, menu)
        m = me.find_elements(By.TAG_NAME, men)
        for n in m:
            if n.text == 'About us':
                n.click()
                break
        self.driver.implicitly_wait(10)
    def Play_Button(self):
        self.driver.find_element(By.XPATH, self.ABOUT_PLAY_BUTTON).click()
        sleep(2)
    def Check_Speaker(self):
        self.driver.find_element(By.XPATH, self.SPEAKER_BUTTON).click()
        sleep(2)
    def Zoom_Button_Check(self):
        self.driver.find_element(By.XPATH, self.ZOOM_BUTTON).click()
        sleep(2)
    def Timer_Check(self):
        self.driver.find_element(By.XPATH, self.TIMER_BUTTON).click()
        sleep(2)
    def Close_Button(self):
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        sleep(2)
    def Free_Screen(self):
        self.driver.find_element(By.XPATH, self.FREEE).click()
        sleep(2)
    def Zoom(self):
        self.driver.find_element(By.XPATH, self.ZOOM_BUTTON).click()
        sleep(2)