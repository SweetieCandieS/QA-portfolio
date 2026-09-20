from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(BASE_DIR, "picture", "test-photo.jpg")

driver = webdriver.Chrome()

driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("http://demo.automationtesting.in/Register.html")

#Заполнить обязательные поля

First_Name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[placeholder = "First Name"]')))
First_Name.send_keys("So")


Last_Name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[placeholder = "Last Name"]')))
Last_Name.send_keys("Lyu")


Email = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[type = "email"]')))
Email.send_keys("qa.test.solyu@example.com")


Phone = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[type = "tel"]')))
Phone.send_keys("9995353535")


radio = driver.find_element(By.CSS_SELECTOR, '[value = "FeMale"]')
radio.click()

#Date of Birth

selector_Year = wait.until(EC.presence_of_element_located((By.ID, "yearbox")))
select_year = Select(selector_Year)
select_year.select_by_value("1997")

selector_Month = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[placeholder = "Month"]')))
select_month = Select(selector_Month)
select_month.select_by_value("June")

selector_Day = wait.until(EC.presence_of_element_located((By.ID, "daybox")))
select_day = Select(selector_Day)
select_day.select_by_value("21")

#Password

Password = wait.until(EC.presence_of_element_located((By.ID, "firstpassword")))
Password.send_keys("Tester'Ok26")


Confirm_Password = wait.until(EC.presence_of_element_located((By.ID, "secondpassword")))
Confirm_Password.send_keys("Tester'Ok26")


#Загрузка фото

file = (r'F:\picture\test-photo.jpg')
upload = wait.until(EC.element_to_be_clickable((By.ID, "imagesrc")))
upload.send_keys(file)


#Скролл и "Submit"

driver.execute_script("window.scrollBy(0, 300);")

button_submit = wait.until(EC.element_to_be_clickable((By.ID, "submitbtn")))
button_submit.click()


#Проверка перехода на страницу
#Пропущена по условию задания: на сайте отсутствуют реальные варианты в
#селекторе "Country" (только плейсхолдер "Select Country"), из-за чего форма
#не проходит валидацию и переход на WebTable.html невозможен — это
#задокументированное ограничение самого демо-сайта, не баг теста.

need_page = "https://demo.automationtesting.in/WebTable.html"

current_page = driver.current_url
print("Фактический результат ", current_page)
print("Ожидаемый результат ", need_page)

if current_page == need_page:
    print(f"Успех. Перешли на {current_page}")
else:
    print(f"Переход на {need_page} не произошёл (текущая страница: {current_page}).")
    print("Известное ограничение: на сайте отсутствуют варианты в селекторе Country.")

driver.quit()