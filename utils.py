import time
from datetime import datetime

from selenium.webdriver.common.by import By


def get_numero_ligacoes(driver, numero):
    linhas = []
    search = driver.find_element(
        By.XPATH,
        value="/html/body/app/ng-component/div/div[1]/div/div/div[1]/div[2]/div[2]/div/input",
    )
    search.clear()
    search.send_keys(numero)
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
    table = driver.find_element(
        By.XPATH,
        value="/html/body/app/ng-component/div/div[1]/div/div/div[2]/div/callhistoryreport/div/div/div[4]/div/div[2]",
    )

    if table:
        linhas = table.find_elements(By.CSS_SELECTOR, value=".row.scroll-report-row-body")

    return len(linhas)
