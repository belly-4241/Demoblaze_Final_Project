

from selenium import webdriver
class BaseTest():
    driver = webdriver.Chrome('/chromedriver_win32/chromedriver.exe')
    def Base(self):
        self.driver.get("https://www.demoblaze.com/")
        self.driver.maximize_window()
        return self.driver
    def tear_down(self):
        self.driver.quit()
        self.driver.close()