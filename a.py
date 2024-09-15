from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# Set up the Remote WebDriver
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=webdriver.ChromeOptions()
)

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
