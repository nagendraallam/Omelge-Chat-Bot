from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Users\Nagendra Allam\Downloads\chromedriver_win32\chromedriver")
driver.get("http://www.omegle.com")

loginbtn = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[1]/div/div/div[1]/input")
loginbtn.send_keys('Programming')# Add your Interest dialog box

cli=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[2]/img")
cli.click() # Clicking the text Button

privacy_form = driver.find_element_by_xpath('/html/body/div[7]/div/p[1]/label/input')
privacy_form.click()# Clicking on checkbox for terms and condition

privacy_form1 = driver.find_element_by_xpath('/html/body/div[7]/div/p[2]/label/input')
privacy_form1.click()# Clicking on checkbox for terms and condition

contButton = driver.find_element_by_xpath('/html/body/div[7]/div/p[3]/input')
contButton.click()# Clicking on continue

# OMEGLE CHAT BOX LOADS UP
sleep(2)
chatBox = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea")
chatBox.send_keys('You have been talking to a bot and you will never know it')# PASSING ANY TEXT TO TEXTBOX
sleep(2)

sendButton=driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[3]/div/button")
sendButton.click()# SENDING THE MESSAGE

# Repeat the same for any other messages and once done, close the  browser window
driver.close()

