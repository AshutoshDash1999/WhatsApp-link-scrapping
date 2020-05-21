
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import base64
import time

print("Scan the QR code then come here.")
browser = input("Enter your fav. browser(Firefox/Chrome): ")
if browser == "Firefox":
    driver = wd.Firefox()  # open firefox
elif browser == "Chrome":
    driver = wd.Chrome()
else:
    print("Choose between Firefox/Chrome.")

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://web.whatsapp.com/")

try:
    element = wdw(driver, 10).until(
        EC.title_contains("WhatsApp")
        )

    try:
        print("Scan the QR code then proceed.")
        time.sleep(10)
        contact_name = input("Enter the contact/group name \nwhose data you want scrap: ")

        try:
            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(contact_name))
        except Exception as e:
            search_box = driver.find_element_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')
            search_box = wdw(driver, 50).until(
                lambda driver : search_box)
            search_box.click()
            search_box.send_keys(contact_name)
            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(contact_name))
            user = wdw(driver, 50).until(lambda driver: user)

        user.click()
        user_profile = driver.find_element_by_xpath('//div[@class = "_5SiUq"][@role = "button"]')
        user_profile.click()

        user_media_menu = user_profile.find_element_by_xpath('//span[contains(text(), "Media, Links and Docs")]')
        user_media_menu.click()  # click on the "Media,docs and links"

        link_bar = user_media_menu.find_element_by_xpath('//button[@title="Links"]')
        link_bar.click()  # click on "Links" tab
        time.sleep(10)

        links = []  # coverting to set as we dont require repeated links
        elements = driver.find_elements_by_tag_name('a')
        for elem in elements:
            href = elem.get_attribute('href')
            links.append(href)

        links = list(set(links))
        # writing the links list to a file
        with open("whatsapp_links.txt", 'w') as f:
            for link in links:
                f.write(link)
                f.write('\n')
        f.close()

    except Exception as e:
        print(e)
        driver.quit()

finally:
    driver.quit()
