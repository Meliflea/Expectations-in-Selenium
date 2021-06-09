import time
import pytest
# py -m pytest -v --driver Chrome --driver-path C:\chromedriver.exe
# данный путь выше вводим через Terminal PyCharm
# если что-то пошло не так - в терминале вводим exit и снова заданный путьу

def test_petfriends(selenium):
    # Open PetFriends base page:
    selenium.get("https://petfriends1.herokuapp.com/")

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = selenium.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()

    # click existing user button
    btn_exist_acc = selenium.find_element_by_link_text(u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    field_email = selenium.find_element_by_id("email")
    field_email.clear()
    field_email.send_keys("Lilit113@mail.ru")

    # add password
    field_pass = selenium.find_element_by_id("pass")
    field_pass.clear()
    field_pass.send_keys("TushBUBUsh")

    # click submit button
    btn_submit = selenium.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!
    if selenium.current_url == 'https://petfriends1.herokuapp.com/all_pets':
        # Make the screenshot of browser window:
        selenium.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

test_petfriends(driver)

driver.implicitly_wait(8)
driver.get("http://petfriends1.herokuapp.com/all_pets")
myDynamicElement = driver.find_element_by_id("myDynamicElement")

images = pytest.driver.find_elements_by_css_selector('.card-deck.card-img-top')
names = pytest.driver.find_elements_by_css_selector('.card-deck.card-img-top')
descriptions = pytest.driver.find_elements_by_css_selector('.card-deck.card-img-top')

for i in range(len(names)):
  assert images[i].get_attribute('src') != ''
  assert names[i].text != ''
  assert descriptions[i].text != ''
  assert ','in descriptions[i]
  parts = descriptions[i].text.split(",")
  assert len(parts[0]) > 0
  assert len(parts[1]) > 0
