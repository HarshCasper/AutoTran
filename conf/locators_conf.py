#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

#Locators for the footer object(footer_object.py)

footer_menu = "xpath,//ul[contains(@class,'nav-justified')]/descendant::a[text()='%s']"
copyright_text = "xpath,//p[contains(@class,'qxf2_copyright')]"
#----

#Locators for the form object(form_object.py)
username_field = "id,id_username"
password_field = "id,id_password"
login_button = "xpath,//button[text()='Login']"
logout_link = "xpath,//a[@href='/accounts/logout']"
