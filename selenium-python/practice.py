import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import webDriverWait
from selenium.common.exceptions import TimeoutException
import pyautogui
from selenium.webdriver.support.ui import Select

# options = webdriver.ChromeOptions()
# options.headless = True
# driver = webdriver.Chrome(options=options)
# driver.get('https://demoqa.com')
# print(driver.title)
# driver.get_screenshot_as_file
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://secondhand.binaracademy.org/")
# # frame
# driver.get('https://the-internet.herokuapp.com/nested_frames')
# driver.switch_to.frame('frame-top')
# driver.switch_to.frame('frame-left')
# text1=driver.find_element(By.XPATH,'/html/body').text
# print(text1)
# driver.switch_to.parent_frame()
# driver.switch_to.frame('frame-left')
# text2=driver.find_element(By.XPATH,'//*[@id="content"]').text
# print(text2)

# # selection box
# driver.get('https://demoqa.com/select-menu')
# # old style
# pilih=Select(driver.find_element(By.ID,'oldSelectMenu'))
# pilih.select_by_visible_text('Yellow')
# pilih.select_by_value('10')
# # select one with typing
# driver.find_element(By.ID,'selectone').click()
# pyautogui.typewrite('prof.')
# pyautogui.press('enter')

# # datepicker1
# driver.get("https://jqueryui.com/datepicker/")
# # cara1
# driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="content"]/iframe'))
# driver.find_element(By.ID,"datepicker").click()
# driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[6]/a').click()
# # cara2
# driver.find_element(By.ID,'datepicker').send_keys('02/01/2021')
# time.sleep(3)
# driver.find_element(By.ID,'datepicker').click()
# # datepicker2
# driver.get("https://demoqa.com/date-picker")
# driver.find_element(By.ID,'datePickerMonthYearInput').click()
# pyautogui.press('backspace',presses=10)
# time.sleep(3)
# driver.find_element(By.ID,'datePickerMonthYearInput').send_keys('02/01/2023')

# # drag&drop
# driver.get("https://demoqa.com/droppable")
# driver.implicitly_wait(10)
# elemen =driver.find_element(By.ID,'draggable')
# kotak =driver.find_element(By.ID,'droppable')
# action=ActionChains(driver)
# action.drag_and_drop(elemen,kotak).perform

# #upload 1
# driver.get("https://demoqa.com/upload-download")
# driver.find_element(By.ID,'uploadFile').send_keys("D:/QA/test.pdf")
# #upload 2
# driver.get("https://gofile.io/uploadFiles")
# driver.find_element(By.ID,'dropZoneBtnSelect').click()
# time.sleep(3)
# pyautogui.write(r"D:\QA\test.pdf")
# pyautogui.press("enter")

# driver.get("https://demoqa.com/menu")
# driver.implicitly_wait(10)
# #cara 1
# menu = driver.find_element(By.LINK_TEXT,'Main Item 2')
# Hover = ActionChains(driver).move_to_element(menu)
# Hover.perform()

# #cara 2
# ActionChains(driver).move_to_element((driver.find_element(By.LINK_TEXT,'Main Item 2'))).perform

# try:
#     webDriverWait(driver,5).until(EC.visibility_of_element_located(By.XPATH,'/html/body/div[1]'))
#     print("pop up muncul")
#     driver.find_element(By.CLASS_NAME,'modalclose').click()
#     print("pop up di close")
    
# except TimeoutException:
#     print("pop up tidak muncul")
#     pass

driver.find_element(By.XPATH, "//a[contains(.,'Masuk')]").click()
time.sleep(3)
driver.find_element(By.ID, "user_email").send_keys("pyth1@gmail.com")
driver.find_element(By.ID, "user_password").send_keys("12345")
time.sleep(3)

# driver.quit()
