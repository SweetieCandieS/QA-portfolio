from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("http://demo.automationtesting.in/WebTable.html")

#"SwitchTo" - > "Alerts"

button_SwitchTo = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "SwitchTo")))
button_SwitchTo.click()

button_Alerts = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Alerts")))
button_Alerts.click()

#"click the button..."

red_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-danger")))
red_button.click()
time.sleep(3)

# Alert

alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
alert.accept()

if alert_text == "I am an alert box!":
    print('Success: "I am an alert box!"')
else:
    print("Error")

current_page = driver.current_url
print("Адрес текущей ссылки: ", current_page)

#Новая вкладка 2

driver.execute_script("window.open();")
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.get("https://demo.automationtesting.in/Alerts.html")

#Confirm

button_AlertCancel = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li:nth-child(2) > .analystic")))
button_AlertCancel.click()

blue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))
blue_button.click()
time.sleep(3)

confirm = driver.switch_to.alert
confirm.dismiss()

#Новая вкладка 3

driver.execute_script("window.open();")
driver.switch_to.window(driver.window_handles[-1])
driver.get("https://demo.automationtesting.in/Alerts.html")

#Prompt

button_AlertTextbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li:nth-child(3) > .analystic")))
button_AlertTextbox.click()

ocean_blue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-info")))
ocean_blue_button.click()
time.sleep(3)

prompt = driver.switch_to.alert
prompt.send_keys("Ура! Задание выполнено!")
prompt.accept()

driver.quit()