import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Abrir una nueva pestaña
driver.execute_script("window.open('https://www.google.com/cucaracha')")
driver.switch_to.window(driver.window_handles[1])
# assert "Python" in driver.title

time.sleep(5)
""" elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source """
driver.close()