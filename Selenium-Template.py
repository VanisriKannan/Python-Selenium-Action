from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


gecko_path = "/home/vanisri/Documents/geckodriver"
service = Service(executable_path=gecko_path)
browser = webdriver.Firefox(service=service)  

browser.maximize_window()
browser.get("https://www.uts.edu.au/")

try:
    browser.find_element(By.XPATH, "/html/body/div[1]/header/div[4]/nav/ul/li[1]/span").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/article/dev/ul/li[5]/div/div[2]/a").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/article/div/div/div[2]/div/main/div[3]/div/div/section[2]/h3").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/article/div/div/div[2]/div/main/div[3]/div/div/section[2]/div/p[5]/a").click()
    browser.find_element(By.ID, "tfa_1").send_keys("John")
    browser.find_element(By.ID, "tfa_2").send_keys("Smith")
    browser.find_element(By.ID, "tfa_3").send_keys("john.smith@gmail.com")
    browser.find_element(By.ID, "tfa_4").send_keys("123456789")
    browser.find_element(By.ID, "tfa_73-L").click()
    browser.find_element(By.ID, "tfa_6-L").click()
    browser.find_element(By.ID, "tfa_55-L").click()
    browser.find_element(By.ID, "tfa_13").send_keys("The quick brown fox jumps over the lazy dog?")
    browser.find_element(By.ID, "tfa_80-L").click()


finally: 
 browser.close()
#done!