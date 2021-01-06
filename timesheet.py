from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from config import ms_username,sso_username, ms_password
from config import dayforce
import time
import traceback


def clocker(button):
    """ Function that clocks me into and out of work as well as lunch using selenium."""

    path = 'C:\\Program Files (x86)\\chromedriver.exe'

    driver = webdriver.Chrome(path)

    driver.maximize_window()
    driver.get(dayforce)

    try:
    
        sso_username_id = 'username'
        sso_pwd_id = 'password'

        sso_sign_in_elem = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, sso_username_id))
        )

        sso_sign_in = driver.find_element_by_id(sso_username_id)
        sso_sign_in.send_keys(sso_username) 

        sso_sign_in_pwd = driver.find_element_by_id(sso_pwd_id)
        sso_sign_in_pwd.send_keys(ms_password)
        sso_sign_in_pwd.send_keys(Keys.RETURN)

        
        duo_push_elem = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'duo_iframe'))
        )

        driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
        duo_push = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/form/div[1]/fieldset/div[1]/button')
        duo_push.click()

        duo_push_elem = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'timeClockButtons'))
        )

        button_to_find = driver.find_element_by_id(button)
        button_to_find.click()

        driver.quit()

    except:
        print(traceback.format_exc())

    finally:
        time.sleep(500)
        driver.quit()