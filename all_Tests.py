import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
import allure
import pytest
def test_Home_phone():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Home':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//a[contains(text(),'Phones')]").click()
    sleep(3)
    driver.find_element(By.XPATH, "//a[contains(text(),'Samsung galaxy s6')]" ).click()
    sleep(3)
    driver.find_element(By.XPATH, "//a[contains(text(),'Add to cart')]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    sleep(3)
    driver.execute_script("window.history.go(-3)")
    sleep(3)
    driver.find_element(By.XPATH, "//a[@id='cartur']").click()
    sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]").click()
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys("belay")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='country']").send_keys("israel")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='city']").send_keys("beersheva")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='card']").send_keys("12334")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='month']").send_keys("jua")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='year']").send_keys("1996")
    sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Purchase')]").click()
    sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'OK')]").click()
    sleep(3)


def test_Home_laptop():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Home':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//a[contains(text(),'Laptops')]").click()
    sleep(3)
    driver.find_element(By.XPATH, "//a[contains(text(),'MacBook air')]").click()
    sleep(3)
    driver.find_element(By.XPATH, "//a[contains(text(),'Add to cart')]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    sleep(3)
    driver.execute_script("window.history.go(-3)")
    sleep(3)
    driver.find_element(By.XPATH, "//a[@id='cartur']").click()
    sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]").click()
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys("belay")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='country']").send_keys("israel")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='city']").send_keys("beersheva")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='card']").send_keys("12334")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='month']").send_keys("jua")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='year']").send_keys("1996")
    sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Purchase')]").click()
    sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'OK')]").click()
    sleep(3)


def test_Home_Monitors():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Home':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//a[contains(text(),'Monitors')]").click()
    sleep(3)
    driver.find_element(By.XPATH, "//a[contains(text(),'ASUS Full HD')]").click()
    sleep(3)
    driver.find_element(By.XPATH, "//a[contains(text(),'Add to cart')]").click()
    sleep(3)
    driver.switch_to.alert.accept()
    sleep(3)
    driver.execute_script("window.history.go(-3)")
    sleep(3)
    driver.find_element(By.XPATH, "//a[@id='cartur']").click()
    sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]").click()
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys("belay")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='country']").send_keys("israel")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='city']").send_keys("beersheva")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='card']").send_keys("12334")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='month']").send_keys("jua")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='year']").send_keys("1996")
    sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Purchase')]").click()
    sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'OK')]").click()
    sleep(3)

def test_Side_button():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Home':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//body/nav[@id='narvbarx']/div[@id='contcar']/div[@id='carouselExampleIndicators']/a[2]/span[1]").click()
    sleep(3)
def test_side_button():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Home':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,
                        "//body/nav[@id='narvbarx']/div[@id='contcar']/div[@id='carouselExampleIndicators']/a[1]/span[1]").click()
    sleep(3)

def test_next_button():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Home':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//button[@id='next2']").click()
    sleep(3)

def test_pre_button():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Home':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//button[@id='prev2']").click()
    sleep(3)
def test_Contactus():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Contact':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@id='recipient-email']").send_keys("belly@gmail.com")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='recipient-name']").send_keys("belay")
    sleep(3)
    driver.find_element(By.XPATH, "//textarea[@id='message-text']").send_keys("i want to staffmate with your company")
    sleep(3)
    driver.find_element(By.XPATH,"//button[contains(text(),'Send message')]").click()
    sleep(3)
    driver.switch_to.alert.accept()

def test_Contactus_Empty_ContactEmail():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Contact':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@id='recipient-email']").send_keys("")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='recipient-name']").send_keys("belay")
    sleep(3)
    driver.find_element(By.XPATH, "//textarea[@id='message-text']").send_keys("i want to staffmate with your company")
    sleep(3)
    driver.find_element(By.XPATH,"//button[contains(text(),'Send message')]").click()
    sleep(3)
    driver.switch_to.alert.accept()

def test_Contactus_Empty_ContactName():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Contact':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@id='recipient-email']").send_keys("belly@gmail.com")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='recipient-name']").send_keys("")
    sleep(3)
    driver.find_element(By.XPATH, "//textarea[@id='message-text']").send_keys("i want to staffmate with your company")
    sleep(3)
    driver.find_element(By.XPATH,"//button[contains(text(),'Send message')]").click()
    sleep(3)
    driver.switch_to.alert.accept()
def test_Contactus_Empty_Message():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Contact':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@id='recipient-email']").send_keys("belly@gmail.com")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='recipient-name']").send_keys("belay")
    sleep(3)
    driver.find_element(By.XPATH, "//textarea[@id='message-text']").send_keys("")
    sleep(3)
    driver.find_element(By.XPATH,"//button[contains(text(),'Send message')]").click()
    sleep(3)
    driver.switch_to.alert.accept()
def test_Contactus_Empty_CoEmailName():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Contact':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@id='recipient-email']").send_keys("")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='recipient-name']").send_keys("")
    sleep(3)
    driver.find_element(By.XPATH, "//textarea[@id='message-text']").send_keys("i want to staffmate with your company")
    sleep(3)
    driver.find_element(By.XPATH,"//button[contains(text(),'Send message')]").click()
    sleep(3)
    driver.switch_to.alert.accept()
def test_Contactus_Empty_CoEmMe():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Contact':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@id='recipient-email']").send_keys("")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='recipient-name']").send_keys("belay")
    sleep(3)
    driver.find_element(By.XPATH, "//textarea[@id='message-text']").send_keys("")
    sleep(3)
    driver.find_element(By.XPATH,"//button[contains(text(),'Send message')]").click()
    sleep(3)
    driver.switch_to.alert.accept()
def test_Contactus_Empty_ConNaMe():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Contact':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@id='recipient-email']").send_keys("belly@gmail.com")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='recipient-name']").send_keys("")
    sleep(3)
    driver.find_element(By.XPATH, "//textarea[@id='message-text']").send_keys("")
    sleep(3)
    driver.find_element(By.XPATH,"//button[contains(text(),'Send message')]").click()
    sleep(3)
    driver.switch_to.alert.accept()
def test_Contactus_Empty_All():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Contact':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@id='recipient-email']").send_keys("")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='recipient-name']").send_keys("")
    sleep(3)
    driver.find_element(By.XPATH, "//textarea[@id='message-text']").send_keys("")
    sleep(3)
    driver.find_element(By.XPATH,"//button[contains(text(),'Send message')]").click()
    sleep(3)
    driver.switch_to.alert.accept()


def test_Aboutus():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'About us':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//body/div[@id='videoModal']/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]").click()
    sleep(3)
def test_Aboutus_PauseButton():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'About us':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//body/div[@id='videoModal']/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]").click()
    sleep(3)
    driver.find_element(By.XPATH, "//body/div[@id='videoModal']/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/button[1]/span[1]").click()
    sleep(3)
def test_Aboutus_Speaker_Button():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'About us':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//body/div[@id='videoModal']/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]").click()
    sleep(3)
    driver.find_element(By.XPATH, "//body/div[@id='videoModal']/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[1]/button[1]/span[1]").click()
    sleep(3)
def test_Aboutus_Zoom_Button():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'About us':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//body/div[@id='videoModal']/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]").click()
    sleep(3)
    driver.find_element(By.XPATH, "//body/div[@id='videoModal']/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/button[4]/span[1]").click()
    sleep(3)

def test_Aboutus_Timer_Button():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'About us':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//body/div[@id='videoModal']/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]").click()
    sleep(3)
    driver.find_element(By.XPATH, "//body/div[@id='videoModal']/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[5]").click()
    sleep(3)

def test_Aboutus_Close_Button():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'About us':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//body/div[@id='videoModal']/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]").click()
    sleep(3)
    driver.find_element(By.XPATH, "//body/div[@id='videoModal']/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[5]").click()
    sleep(3)
    driver.find_element(By.XPATH, "//body/div[@id='videoModal']/div[1]/div[1]/div[3]/button[1]").click()
    sleep(3)

def test_Cart_Delete():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Cart':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//a[contains(text(),'Delete')]").click()
    sleep(3)

def test_Login():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Log in':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@id='loginusername']").send_keys("belay")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='loginpassword']").send_keys("4241@")
    sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()
    sleep(3)
    driver.switch_to.alert.accept()

def test_Signup():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Sign up':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@id='sign-username']").send_keys("belay")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='sign-password']").send_keys("4241@")
    sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Sign up')]").click()
    sleep(3)
    driver.switch_to.alert.accept()

def test_invalid_username_Login():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Log in':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@id='loginusername']").send_keys("mitana")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='loginpassword']").send_keys("4241@")
    sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()
    sleep(3)
    driver.switch_to.alert.accept()

def test_invalid_Password_Login():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Log in':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@id='loginusername']").send_keys("belay")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='loginpassword']").send_keys("4142")
    sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()
    sleep(3)
    driver.switch_to.alert.accept()
def test_empty_username_Login():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Log in':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@id='loginusername']").send_keys("")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='loginpassword']").send_keys("4241@")
    sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()
    sleep(3)
    driver.switch_to.alert.accept()

def test_Empty_Password_Login():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Log in':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@id='loginusername']").send_keys("mitana")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='loginpassword']").send_keys("")
    sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()
    sleep(3)
    driver.switch_to.alert.accept()

def test_EmUsername_EmPassword_Login():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/')
    sleep(3)
    time.sleep(3)
    driver.maximize_window()
    menu = " //body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'Log in':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@id='loginusername']").send_keys("")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='loginpassword']").send_keys("")
    sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()
    sleep(3)
    driver.switch_to.alert.accept()





















