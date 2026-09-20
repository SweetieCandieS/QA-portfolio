from selenium.webdriver.common.by import By
import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.saucedemo.com/")
time.sleep(3)

username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

button_log = driver.find_element(By.ID, "login-button")
button_log.click()


button_backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
button_backpack.click()

button_BikeLight = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
button_BikeLight.click()

button_onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
button_onesie.click()

button_cart = driver.find_element(By.ID, "shopping_cart_container")
button_cart.click()

items_count = driver.find_elements(By.CLASS_NAME, "cart_item")
time.sleep(3)

if len(items_count) == 3:
    print("В корзине 3 товара")

else:
    print("Ошибка. Количество товаров в корзине: " + str(len(items_count)))

driver.quit()

