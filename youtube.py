# Import necessary modules
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Configure Chrome options
opt = Options()
opt.add_argument("start-maximized")  # Maximize the browser window when it opens
opt.add_experimental_option("detach", True)  # Allow the browser window to be detached
opt.add_argument("disable-web-security")  # Disable web security (use with caution)
opt.add_argument("allow-running-insecure-content")  # Allow running insecure content (use with caution)

# Create a Chrome WebDriver instance with the specified options
driver = webdriver.Chrome(options=opt)

# Open the specified URL in the Chrome browser
driver.get("https://www.youtube.com/@mass-respect/shorts")

# Pause the script execution for 2 seconds to allow the page to load
sleep(2)

# Set up variables for scrolling
scroll_increment = 1000  # Scroll down by 1000 pixels each time
total_scrolls = 22  # Scroll a total of 22 times

# Perform scrolling to load more content on the page
for _ in range(total_scrolls):
    # Scroll down by the specified increment using JavaScript
    driver.execute_script(f"window.scrollBy(0, {scroll_increment});")

    # Add a delay of 2 seconds to simulate human-like scrolling behavior
    sleep(2)

# Find all the links (video titles) on the page using an XPath expression
links = driver.find_elements(By.XPATH, '//*[@id="details"]/h3/a')

# Initialize a list to store the href attributes of the links
hrefs = []

# Iterate through the found links and extract their href attributes
for element in links:
    href = element.get_attribute("href")
    hrefs.append(href)

print(hrefs)
# Print the total number of hrefs found
print(len(hrefs))

driver.quit()