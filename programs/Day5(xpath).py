"""
8.xpath
"""
"""
*path of an element present in html tree structure is called as xpath.
*xpath is classified into 2 types,
1.absolute xpath
2.relative xpath

1.absolute xpath:
*****************
*absolute xpath indicate by "single forward slash(/)".
*"/" --> traverse from parent to immediate child.

drawback of absolute xpath:
===========================
*xpath will be lengthly compratively relative xpath.
*always we should traverse from parent to immediate child only.
*to over come this drawback we go relative xpath

2.relative xpath:
*****************
*relative xpath indicates by "double forward slash(//)".
*"//" --> traverse from parent to any of its child.
"""
#####################################################################################################################################
#18-08-2023
"""
xpath by attribute:
*******************
*inspecting an element by specifying attribute in xpath.
*if a html code consist of attribute then we can go xpath by attribute,
syntax:
=======
//tag-name[@attribute-name = 'attribute-value']

sample code:
============
<a href="https://www.fb.com"  id="a1"   name="n1">  FaceBook </a>

example:
========
//a[@href='https://www.fb.com']
//a[@id='a1']
//a[@name='n1']

#xath to inspect recuitement in ksrtc
//a[@title='Recruitment']

#xath to inspect from place in ksrtc
//input[@name='fromPlaceName']

#xath to inspect ayurveda in 1mg
//a[@data-vars-event-label='Ayurveda']

#xath to inspect search text in flipkart
//span[@class='title-text']

#xath to inspect sunglass in lenskart
//div[@class='MuiBox-root jss1358']

xpath with multiple attribute:
******************************
*xpath by single attribute is matches with multiple elements then we can specify multiple
attributes that is called as xpath with multiple attribute.
syntax:
-------
//tag-name[@attribute1='attribute1-value' and @attribute2='attribute3-value' .... ]

#xath to inspect mobiles in amazon
//a[@class='nav-a  ' and @data-csa-c-content-id='nav_cs_mobiles']

#xath to inspect pomegrants in ajiomart
//a[@class='LastRowLink--1klhk6r jpBosF getGaData' and @id='lrd5']


xpath with group by indexing:
*****************************
*if any xpath is matches with multiple elements and we want a specific element then we go xpath by
group by indexing.
*group by the xpath in round brackets() and provide index[](index starts from 1)

syntax:
-------
(xpath)[index]

#xath to inspect login in myntra
(//a[@class='styles__login-link___2PwqA'])[2]

#xath to inspect collor in myntra
(//a[@class='zoom-text'])[2]

#xath to inspect ibaco 
(//a[@href='our-products.php'])[1]

#xath to inspect shampoo in nykka
(//div[@class='plp-card-details-name line-clamp jm-body-xs jm-fc-primary-grey-80'])[3]

#xath to inspect sale in decathlon
(//span[@class='!mr-0'])[1]
"""
from selenium.webdriver import Chrome
from time import sleep

#example on xpath in myntra.com
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.myntra.com/kids?f=Categories%3AShirts%3A%3AGender%3Aboys%2Cboys%20girls&plaEnabled=false")
driver.maximize_window()
driver.find_element("xpath", "(//h4[@class='atsa-title'])[3]").click()
"""
############################################################################################################################
#19-05-2023
"""
xpath by text() function:
*************************
*if html code consist of text value then we can go xpath by text function.
*text value is case-senstive.
*text() function can replace with dot(.).

syntax:
-------
//tagname[text()='text_value']
                (or)
//tagname[.='text_value']


#xpath to inspect men tab in myntra
(//a[text()='Men'])[1]    #(//a[.='Men'])[1]

#xpath to inspect profile in myntra 
//span[.='Profile']

#xpath to inspect login/signup in mytra 
//a[.='login / Signup']

#xpath to inspect stable version of python in selenium.dev
//a[.='4.11.2 (August 01, 2023)']
"""
#ws to click on login in zomato
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.zomato.com/bangalore")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Log in']").click()
"""

#ws to automate pharmacy in medplus
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.medplusmart.com/")
driver.maximize_window()
driver.find_element("xpath", "//h6[.='Pharmacy']").click()
driver.find_element("xpath", "//a[.='Upload your Prescription']").click()
driver.find_element("xpath", "//input[@name='mobileNumber']").send_keys("7688663345")
driver.find_element("xpath", "//button[.='Send OTP']").click()
"""
########################################################################################################################
"""
xpath with partial dynamic element:
***********************************
*a part/portion of an element is keep on changing is called as partial dynamic element.
*complete element will not keep on changing only a part of an element is keep on changing.
*to handle this kind of element we go contains() function.
*when the "attribute-value and text-value is very lengthy" then also we will go contains().

syntax of attribute in conatins() function :
--------------------------------------------
//tag-name[contains(attribute-name , 'attribute-value')]

syntax of text in conatins() function :
---------------------------------------
//tag-name[contains(. , 'text-value')]

examples:
=========
xpath to inspect python stable version in selenium.dev
//a[contains(.,'4.11.2')]
"""

"""
assignment:
-----------
launch passport seva application
https://www.passportindia.gov.in/AppOnlineProject/welcomeLink#
click on new registration --> enter all details and click on regsiter button

launch spotify application
https://open.spotify.com/
click on signup --> enter all details and click on signup
"""

















