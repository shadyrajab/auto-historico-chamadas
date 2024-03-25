import os
import time
from datetime import datetime

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

load_dotenv()

URL = os.getenv("URL")
USERNAME = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

service = Service(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(URL)

username = driver.find_element(By.NAME, value="login")
password = driver.find_element(By.NAME, value="password")

username.send_keys(USERNAME)
password.send_keys(PASSWORD)


button = driver.find_element(By.XPATH, value='//*[@id="botao_entrar"]/button')
button.click()

time.sleep(10)

relatorios = driver.find_element(By.XPATH, value='//*[@id="navbar"]/ul/li[4]/a')

relatorios.click()

time.sleep(10)

select_box = Select(
    driver.find_element(
        By.XPATH,
        value="/html/body/app/ng-component/div/div/div/div/div[1]/div[2]/div[1]/div/select",
    )
)


select_box.select_by_visible_text("Histórico de Chamadas")


search = driver.find_element(
    By.XPATH,
    value="/html/body/app/ng-component/div/div[1]/div/div/div[1]/div[2]/div[2]/div/input",
)

search.send_keys("61999273832")


now = datetime.now().strftime("%d/%m/%Y")

data_inicio = driver.find_element(
    By.XPATH,
    value="/html/body/app/ng-component/div/div[1]/div/div/div[1]/div[2]/div[3]/div/div/input",
)

data_inicio_calendar_button = driver.find_element(
    By.XPATH,
    value="/html/body/app/ng-component/div/div[1]/div/div/div[1]/div[2]/div[3]/div/div/button",
)

data_fim = driver.find_element(
    By.XPATH,
    value="/html/body/app/ng-component/div/div[1]/div/div/div[1]/div[2]/div[4]/div/div/input",
)

data_fim_calendar_button = driver.find_element(
    By.XPATH,
    value="/html/body/app/ng-component/div/div[1]/div/div/div[1]/div[2]/div[4]/div/div/button",
)


data_inicio.send_keys(now)
data_fim.send_keys(now)
data_inicio_calendar_button.click()
data_fim_calendar_button.click()


consultar = driver.find_element(
    By.XPATH,
    value="/html/body/app/ng-component/div/div[1]/div/div/div[1]/div[2]/div[5]/div/button",
)

consultar.click()

time.sleep(10)

linhas = driver.find_elements(By.CSS_SELECTOR, value=".row.scroll-report-row-body")

print(len(linhas))
