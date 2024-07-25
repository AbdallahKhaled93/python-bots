from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver_path = '/usr/bin/chromedriver'  
login_url = 'https://sso.anef.dgef.interieur.gouv.fr/auth/realms/anef-usagers/protocol/openid-connect/auth?client_id=anef-usagers&theme=portail-anef&redirect_uri=https%3A%2F%2Fadministration-etrangers-en-france.interieur.gouv.fr%2Fparticuliers%2F%23&response_mode=fragment&response_type=code&scope=openid&acr_values=eidas1'  

driver = webdriver.Chrome()
driver.get(login_url)

username_field = driver.find_element(By.ID, "login")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys("")
password_field.send_keys("")

submit_button = driver.find_elements(By.XPATH, "//button[@type='submit']")
submit_button[0].click()

WebDriverWait(driver, 50000).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='ui-menuitem-text ng-star-inserted']")))

dropdown_menu = driver.find_element(By.XPATH, "//span[@class='ui-menuitem-text ng-star-inserted']")
dropdown_menu.click()

acceder_mon_compte_button = driver.find_elements(By.XPATH, "//a[@href='#/espace-personnel/mon-compte']")
acceder_mon_compte_button[0].click()

WebDriverWait(driver, 50000).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='ui-tabview-title ng-star-inserted']")))
demande_tabs = driver.find_elements(By.XPATH, "//span[@class='ui-tabview-title ng-star-inserted']")
demande_tabs[2].click()

WebDriverWait(driver, 50000).until(EC.visibility_of_element_located((By.XPATH, "//li[@class='stepsBox--item active']")))
active_step = driver.find_elements(By.XPATH, "//li[@class='stepsBox--item active']")

print(active_step[0].text)
