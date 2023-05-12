# This script autoloads and closes a webpage. It can be integrated to test 
# functionality of a webpage. The example checks to ensure "certifications"
# is present on my github page. 

from selenium import webdriver
from time import sleep

# Define words to find
findme = ["Bio", "Certifications", "Connect with me", "Languages and Tools"]
for i in findme:
    driver = webdriver.Firefox()
    driver.get("https://github.com/TimRohr")
    sleep(3)
    if i in driver.page_source:
        print(i, " was found on the page")
    # If writting unit tests, you would want something like the below commented line instead:
    # assertTrue(i in drive.page_source)
    driver.close()