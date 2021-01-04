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

path = 'C:\\Program Files (x86)\\chromedriver.exe'

driver = webdriver.Chrome(path)

driver.maximize_window()
driver.get(dayforce)


try:
   
    sso_username_id = 'username'
    sso_pwd_id = 'password'

    sso_sign_in_elem = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, sso_username_id))
    )

    sso_sign_in = driver.find_element_by_id(sso_username_id)
    sso_sign_in.send_keys(sso_username) 

    sso_sign_in_pwd = driver.find_element_by_id(sso_pwd_id)
    sso_sign_in_pwd.send_keys(ms_password)
    sso_sign_in_pwd.send_keys(Keys.RETURN)

    
    duo_push_elem = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'duo_iframe'))
    )


    driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
    duo_push = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/form/div[1]/fieldset/div[1]/button')
    duo_push.click()

    duo_push_elem = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'timeClockButtons'))
    )

    clock_in_id = 'dijit__Widget_18'
    clock_out_id = 'dijit__Widget_19'
    meal_start_id = 'dijit__Widget_24'
    meal_end_id = 'dijit__Widget_26'


    clock_in = driver.find_element_by_id(clock_in_id)
    clock_in.click()

    time.sleep(10)

    clock_out = driver.find_element_by_id(clock_out_id)
    clock_out.click()




except:
    print(traceback.format_exc())

finally:
    time.sleep(500)
    driver.quit()



"""next_bttn_id = 'idSIButton9'
sso_username_id = 'username'
sso_pwd_id = 'password'

try:
    sign_in_elem = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "i0116"))
    )

    sign_in = driver.find_element_by_id('i0116')
    sign_in.send_keys(ms_username)

    next_bttn = driver.find_element_by_id(next_bttn_id)
    next_bttn.click()

    sso_sign_in_elem = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, sso_username_id))
    )

    sso_sign_in = driver.find_element_by_id(sso_username_id)
    sso_sign_in.send_keys(sso_username) 

    sso_sign_in_pwd = driver.find_element_by_id(sso_pwd_id)
    sso_sign_in_pwd.send_keys(ms_password)
    sso_sign_in_pwd.send_keys(Keys.RETURN)

    #actions = ActionChains(driver)
    #ctions.move_to_element_with_offset(driver.find_element_by_id('duo_iframe'), 0,0)
    #actions.move_by_offset(406, 38).click().perform()



    duo_push_elem = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'duo_iframe'))
    )


    driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
    duo_push = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/form/div[1]/fieldset/div[1]/button')
    duo_push.click()

    ms_no_bttn_id = 'idBtn_Back'
    ms_no_bttn = driver.find_element_by_id(ms_no_bttn_id)
    ms_no_bttn.click()


    #quick_links_class_name = 'static dynamic-children menu-item ms-core-listMenu-item ms-displayInline ms-navedit-linkNode'


    # Script breaks here, won't click the send me a push button for some reason, it cant locate it.
    #driver.implicitly_wait(15)
    
    # /html/body/div/div/div[1]/div/form/div[1]/fieldset/div[1]/button
    #duo_push = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/form/div[1]/fieldset/div[1]/button')
    #duo_push.click()

except:
    print(traceback.format_exc())

finally:
    time.sleep(500)
    driver.quit()"""


