from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# para que el navegador no se abra
options = ChromeOptions() 
options.add_argument("--headless")
service = Service(executable_path=r"C:\Program Files\chromedriver\chromedriver.exe")
driver = Chrome(service=service,
                  options=options)

driver.get('https://www.zonaprop.com.ar/casas-ph-terrenos-venta-capital-federal-mas-400-m2-menos-300000-dolar.html')


selector =  'CardContainer-sc-1tt2vbg-5 fvuHxG'
links = WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

for i in range(len(links))[0:3]:
    print(links[i].text)

