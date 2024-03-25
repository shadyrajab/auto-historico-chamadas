import json
import os
import time
from datetime import datetime

import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utils import add_chamada, get_numero_ligacoes

load_dotenv()

URL = os.getenv("URL")
USERNAME = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
EQUIPE_FLAVIO = json.loads(os.getenv("EQUIPE_FLAVIO"))
TOKEN = os.getenv("TOKEN")

service = Service(executable_path="chromedriver.exe")
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

now = datetime.now().strftime("%d-%m-%Y")
obj = []

for nome, numero in EQUIPE_FLAVIO:
    qtd = get_numero_ligacoes(driver, numero)

    obj.append({"CONSULTOR": nome, "TELEFONE": numero, "CHAMADAS": qtd})

df = pd.DataFrame(obj)

df.to_excel(f"chamadas {str(now)}.xlsx")
