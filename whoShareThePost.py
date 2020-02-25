# * @file whoShareThePost.py
# * @brief show the person autoimatically who share the post 
# * @author TWC
# * @date 2020-2-22
from selenium import webdriver

# * @brief shield the 'alert window' (like Cookie ..etc.)
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
         }
}
options.add_experimental_option('prefs',prefs)
driver = webdriver.Chrome(chrome_options = options)

# the url of the fan page we want to search
driver.get("")

# type the account and password if necessary
element = driver.find_element_by_id("email").send_keys("")
element = driver.find_element_by_id("pass").send_keys("") 
element = driver.find_element_by_id("loginbutton").click()

# according to the href, the post we want to know that  who share this
element = driver.find_element_by_xpath('//a[contains(@href,"/shares/view/?av=100006480090445")]').click() 