# requirements:- selenium, geckodriver(firefox)/chromedriver(chrome),

from selenium import webdriver as wd  # import library

print("Scan the QR code then come here.")
browser = input("Enter your fav. browser(Firefox/Chrome): ")
if browser == "Firefox":
    driver = wd.Firefox()  # open firefox
elif browser == "Chrome":
    driver = wd.Chrome()
else:
    print("Choose between Firefox/Chrome.")

driver.get("https://web.whatsapp.com/")     # redirect to site
input("Press 'ENTER' for the next step.")

name = input("Enter the contact name here: ")   # enter the name whose links you want to  access
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))  # access the path to contacts chat
user.click()

user_profile = user.find_element_by_xpath('//header[@class="_2y17h"]')
user_profile.click()    # click on the profile

user_media_menu = user_profile.find_element_by_xpath('//span[contains(text(), "Media, Links and Docs")]')
user_media_menu.click()  # click on the "Media,docs and links"

link_bar = user_media_menu.find_element_by_xpath('//button[@title="Links"]')    # click on "Links" tab
link_bar.click()

links = []
elements = driver.find_elements_by_tag_name('a')
for elem in elements:
    href = elem.get_attribute('href')
    links.append(href)
print(links)

# writing the links list to a file
with open("whatsapp_links.txt", 'w') as f:
    for link in links:
        f.write(link)