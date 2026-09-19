from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

path_to_extension = (r'C:\Users\Конфета\AppData\Local\Google\Chrome\User Data\Default\Extensions\omghfjlpggmjjaagoclmmobgdodcjboh\3.93.7_0')

chrome_options = Options()

# Поддержка WebExtension через BiDi
chrome_options.enable_bidi = True
chrome_options.enable_webextensions = True

driver = webdriver.Chrome(options=chrome_options)

#Расширение Browsec. Без VPN сайт не прогружается
result = driver.webextension.install(path=path_to_extension)

driver.maximize_window()
wait = WebDriverWait(driver, 30)

#VPN надо вручную включить
input("Включить VPN и нажать Enter")

first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)

driver.get("https://demo.us.espocrm.com/")

#Часть 1 Login

find_selector = wait.until(EC.presence_of_element_located((By.ID, "field-language")))
select1 = Select(find_selector)
select1.select_by_value("en_GB")

button_login = wait.until(EC.element_to_be_clickable((By.ID, "btn-login")))
button_login.click()

#Часть 3 Task + Selector

menu_task = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Tasks")))
menu_task.click()

find_selector_all = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[title ="Filter"]'))).click()

#Часть 4 Checkbox "Only My"

checkbox_OnlyMy = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.checkbox:nth-child(11)")))
checkbox_OnlyMy.click()

#Часть 5 Checkbox "Select al results"

checkbox_Name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".select-all")))
checkbox_Name.click()

#Часть 6 Button "Actions"

button_Actions = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-group.actions > button.actions-button")))
button_Actions.click()

Mass_Update = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Mass Update")))
Mass_Update.click()

#Часть 7 Проверка Button "Update"

button_update = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-name ="update"]')))
button_update_disabled = button_update.get_attribute("disabled")
print("value of button: ", button_update_disabled)

if button_update_disabled is not None:
    print("Кнопка НЕ активна")
else:
    print("Кнопка активна")

button_close = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "close")))
button_close.click()

#Часть 8 Create Task

button_CreateTask = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Create Task")))
button_CreateTask.click()

Name = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-name="name"]')))
Name.send_keys("Test")

#Часть 9 Проверка селектора "Status"

Status = driver.find_element(By.CSS_SELECTOR, ".selectize-input.items.has-options.full.has-items > [data-value = 'Not Started']")
if Status.get_attribute("data-value") == "Not Started":
    print("True")
else:
    print("False")

#Часть 10 Button "Save"

button_save = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-xs-wide:nth-child(1)")))
button_save.click()
time.sleep(5)


link_Tasks = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[style = "user-select: none;"] > a.action')))
link_Tasks.click()

#Часть 11 Checkbox Task Test

checkbox_Test = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-row:nth-child(1) .record-checkbox-container")))
checkbox_Test.click()

#Часть 12 Button "Actions"

button_Actions = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-group.actions > button.actions-button")))
button_Actions.click()

#Часть 13 "Remove"

Remove = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Remove")))
Remove.click()

button_Remove = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-danger.btn-s-wide")))
button_Remove.click()

driver.quit()
