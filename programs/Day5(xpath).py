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
















