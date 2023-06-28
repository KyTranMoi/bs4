from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Initialize ChromeDriver service
chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())

# Set ChromeDriver options (optional)
chrome_options = webdriver.ChromeOptions()
# Add any desired options here, such as running in headless mode:
# chrome_options.add_argument('--headless')

# Initialize Chrome WebDriver with the service and options
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://www.bing.com/search?form=MY0291&OCID=MY0291&q=Bing+AI&showconv=1')

# Rest of your code...

# Quit the driver when done
driver.quit()
