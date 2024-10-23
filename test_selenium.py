from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# Set up WebDriver (replace with the path where you've stored chromedriver)
driver_path = "chromedriver-win64\chromedriver.exe"
service = Service(driver_path)

# Initialize WebDriver with the Service object
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Find the search box, enter "Selenium", and press Enter
search_box = driver.find_element("name", "q")
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)

# Print the title of the page
print(driver.title)

# Close the browser after the search
driver.quit()
