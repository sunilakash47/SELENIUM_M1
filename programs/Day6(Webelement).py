"""
web-element methods
-------------------
"""
"""
*the return type of find_element() method is web-element.
*an element present in web-page is called as web-element.
*web-element like textfield, radio button, check-box, button , link, dropdown, etc...
*a find_element() method will find the address of an element from a page and it will store in a variable, that variable
refers to as web-element.
*methods of web-elements are,
1.click()
    *it will perform click action on button,link,radio button, check box, tab, etc..
2.send_keys()
    *it is used to enter a data into text field.
3.clear()
    *it is used to remove a value present in text field.
"""

from selenium.webdriver import Chrome
from time import sleep

#ws to click on search field and search for facewash
"""
driver = Chrome()
driver.get("https://mamaearth.in/")
driver.maximize_window()
sleep(5)
src = driver.find_element("xpath", "//p[contains(@class,'styles_typicalWrapper')]")
src.click()
src_txt = driver.find_element("xpath", "//input[@id='searchInputWrapper']")
src_txt.send_keys("facewash")
"""

#ws to clear/remove default value present in text field
"""
driver = Chrome()
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
un = driver.find_element("id", "a1")
un.clear()
un.send_keys("automation user")
"""





































"""
how to launch browser without passing driver executable path:
*************************************************************
*goto below location/path and paste all driver executable files.
C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python311\\Scripts
"""

















































