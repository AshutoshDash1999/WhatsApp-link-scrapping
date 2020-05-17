# requirements:- selenium, geckodriver(firefox)/chromedriver(chrome),

from selenium import webdriver as wd

print("Scan the QR code then come here.")
driver = wd.Firefox()
driver.get("https://web.whatsapp.com/")
input("Press 'ENTER' for the next step.")
name = input("Enter the contact name here: ")
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

user_profile = user.find_element_by_xpath('//header[@class="_2y17h"]')
user_profile.click()

user_media_menu = user_profile.find_element_by
user_media_menu.click()

link = user_media_menu.find_element_by_link_text("Links")
link.click()