from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the driver (make sure you have ChromeDriver installed and in your PATH)
driver = webdriver.Chrome()

# Open Google
driver.get('https://ucam.uiu.ac.bd/Security/LogIn.aspx')

# Wait for the page to load (optional, but helps avoid errors)
time.sleep(2)

# Find the search box
student_id = driver.find_element(By.NAME, 'logMain$UserName')

# Type your query
student_id.send_keys('Your ID')

# Find the search box
student_pass = driver.find_element(By.NAME, 'logMain$Password')

# Type your query
student_pass.send_keys('Your Pass')

# Press Enter
student_id.send_keys(Keys.RETURN)

# Optional: wait to see the results
time.sleep(60)

# Quit the driver
driver.quit()
