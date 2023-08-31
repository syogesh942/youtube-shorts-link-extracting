# youtube-shorts-link-extracting
This Python code uses the Selenium library to automate a web browser (Google Chrome) to interact with a YouTube page. explanation of each section of the code is in README:

1. Import Necessary Modules:
The code starts by importing required modules from Python and Selenium.

2. Configure Chrome Options:
Chrome options are configured using the Options() class from Selenium. These options customize the behavior of the Chrome browser when it's launched.
opt.add_argument("start-maximized") maximizes the browser window when it's opened.
opt.add_experimental_option("detach", True) allows the browser window to be detached from the WebDriver instance.
opt.add_argument("disable-web-security") disables web security (use with caution, not recommended for regular browsing).
opt.add_argument("allow-running-insecure-content") allows running insecure content (use with caution, not recommended for regular browsing).

3. Create a Chrome WebDriver Instance:
It creates a new instance of the Chrome WebDriver using the specified Chrome options.

4. Open a URL:
The WebDriver navigates to the YouTube page specified in driver.get().

5. Pause for Page to Load:
sleep(2) pauses the script execution for 2 seconds to allow the page to load. This is a simple form of waiting for elements to appear on the page.

6. Set Up Variables for Scrolling:
scroll_increment is set to 1000 pixels, which will be used to scroll down the page.
total_scrolls is set to 22, indicating that the page will be scrolled 22 times.

7. Perform Scrolling:
A loop iterates total_scrolls times, simulating scrolling down the page.
driver.execute_script(f"window.scrollBy(0, {scroll_increment});") executes JavaScript to scroll the page down by the specified increment.
sleep(2) adds a 2-second delay between each scroll to simulate human-like scrolling behavior.

8. Find Video Links:
It uses Selenium's driver.find_elements() method with an XPath expression to locate video links (video titles) on the page. The found links are stored in the links list.

9. Extract Href Attributes:
A list hrefs is initialized to store the href attributes of the found links.
A loop iterates through links, extracts the href attribute using element.get_attribute("href"), and appends it to the hrefs list.

10. Print the Extracted Hrefs:
It prints the hrefs list, which contains the URLs of the videos.

11. Print the Total Number of Hrefs Found:
It prints the total number of hrefs found on the page.

12. Quit the WebDriver:
driver.quit() is used to close the Chrome browser and WebDriver instance when the script is done.
