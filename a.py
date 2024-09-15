from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize WebDriver for Chromium (Headless)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run browser in headless mode (no UI)
options.add_argument('--disable-gpu')  # Disable GPU for better performance
options.add_argument('--no-sandbox')  # Sandbox issues with some environments
options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
options.binary_location = '/usr/bin/chromium-browser'  # Path to Chromium

# Set up the ChromeDriver with WebDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # The URL of the page you want to scrape
    url = "http://harihwugsis.kesug.com/get_insta.php"
    driver.get(url)  # Open the page

    # Wait for JavaScript to run and the page to load fully (adjust time if necessary)
    time.sleep(5)

    # Get the page source after the JavaScript has executed
    page_source = driver.page_source

    # Print or save the content
    print(page_source)  # To view it in the console

    # Save the page content to an HTML file
    with open("scraped_content.html", "w", encoding="utf-8") as file:
        file.write(page_source)

finally:
    # Close the browser properly
    driver.quit()
