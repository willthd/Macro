from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# naver의 경우 아이디, 비밀번호 빨리 쳐지면 보안문자 입력하게 되어 있음
driver = webdriver.Chrome('/Users/bagjongsu/Desktop/workingDir/selenium/selenium_prj/chromedriver')
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
element = driver.find_element_by_id("id")
element.send_keys("right_gear")
element = driver.find_element_by_id("pw")
element.send_keys("dhsmfeh1")
element = driver.find_element_by_class_name("btn_global")
element.click()
driver.close()