# requirements:- selenium, geckodriver(firefox)/chromedriver(chrome),

from selenium import webdriver as wd  # import library

print("Scan the QR code then come here.")
driver = wd.Firefox()  # open firefox
driver.get("https://web.whatsapp.com/")     # redirect to site
input("Press 'ENTER' for the next step.")
name = input("Enter the contact name here: ")   # enter the name whose links you want to  access
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))  # access the path to contacts chat
user.click()

user_profile = user.find_element_by_xpath('//header[@class="_2y17h"]')
user_profile.click()    # click on the profile

user_media_menu = user_profile.find_element_by_xpath('//div[@class="_1ZiJ3"]')    # under construction
user_media_menu.click()

link = user_media_menu.find_element_by_xpath('//button[@title="Links"]')    # under construction
link.click()
