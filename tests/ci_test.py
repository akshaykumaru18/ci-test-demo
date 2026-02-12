import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time


options = Options()
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

file_path =  "file:///Users/akshaykumaru/Development/Indian%20Oil%20Training/CICD%20Demo/index.html"
print(file_path)
def test_submit_form():
  
    driver.get(file_path)
    
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "password").send_keys("password")
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    driver.find_element(By.ID, "age").send_keys("25")
    driver.find_element(By.ID, "date").send_keys("2025-01-01")
    driver.find_element(By.ID, "submit").click()
    time.sleep(10)
    assert driver.find_element(By.ID, "message").text == "Form submitted successfully"
    print("Test passed")
    driver.quit()