import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("c:\\chromedriver\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(5)
driver.implicitly_wait(10)
cartitems = driver.find_elements_by_xpath("//div[@class='products']/div")
print(type(cartitems))
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print("No of button is",len(buttons))
list1=[]
for button in buttons:
    print(button)
    list1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list1)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
#code is before applying discount
amount1= driver.find_element_by_css_selector(".discountAmt").text


driver.find_element_by_css_selector(".promocode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector((".promoBtn")).click()
# compare=driver.find_element_by_css_selector(".promoInfo").text
# print(compare)
# assert compare=="Code applied ..!","Promo not applied sucessfu
wait = WebDriverWait(driver,15)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promocode")))
compare=driver.find_element_by_css_selector(".promoInfo").text
print(compare)
assert compare=="Code applied ..!","Promo not applied sucessful"
veggies=driver.find_elements_by_css_selector("p.product-name")
vegname=[]
for v in veggies:
    vegname.append(v.text)
print(vegname)
assert list1==vegname
#driver.close()
amount2= driver.find_element_by_css_selector(".discountAmt").text
print(amount1)
print(amount2)
assert int(amount1) > float(amount2)
veggis_amount =driver.find_elements_by_xpath("//tr//td[5]/p")
amount = 0
for veg in veggis_amount:
    amount += int(veg.text)
print(amount)
driver.close()
#comment below code for sucessful exectution of above code

#code for select
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
driver.find_element_by_xpath("//input[@type='submit']").click()
message = driver.find_element_by_class_name("alert-success").text
assert "success" in message

#using ccs for nth child
driver.find_element_by_xpath("//a[text()='Cancel']").click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)


#code for checkbox/radio
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()
assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()

