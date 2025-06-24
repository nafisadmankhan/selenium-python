from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the driver (make sure you have ChromeDriver installed and in your PATH)
driver = webdriver.Chrome()

# Open Google
driver.get('https://www.google.com/')

# Wait for the page to load (optional, but helps avoid errors)
time.sleep(2)

# Find the search box
search_box = driver.find_element(By.NAME, 'q')

# Type your query
search_box.send_keys('OpenAI ChatGPT')

# Press Enter
search_box.send_keys(Keys.RETURN)

# Optional: wait to see the results
time.sleep(60)

# Quit the driver
driver.quit()
