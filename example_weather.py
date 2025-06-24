from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the driver (make sure you have ChromeDriver installed and in your PATH)
driver = webdriver.Chrome()

# Open Google
driver.get('https://live8.bmd.gov.bd/')

# Wait for the page to load (optional, but helps avoid errors)
time.sleep(2)

# Find the forecast text inside <p> under class "big"
try:
    # Locate the element
    forecast_element = driver.find_element(By.CSS_SELECTOR, '.forecastbox .big p')

    # Get the raw text
    forecast_text = forecast_element.text

    # Replace 'o' with degree symbol (optional cleanup)
    cleaned_text = forecast_text.replace('o', '°')

    print("Forecast:", cleaned_text)

except Exception as e:
    print("Error finding element:", e)

# Optional: wait to see the results
time.sleep(60)

# Quit the driver
driver.quit()
