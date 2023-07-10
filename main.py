from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
import os
from dotenv import load_dotenv
load_dotenv()

# chrome.exe --remote-debugging-port=PORT --user-data-dir="path/chrome/data"

opt = Options()

opt.add_experimental_option('debuggerAddress', os.getenv('URL_PORT'))

driver = webdriver.Chrome(executable_path=os.getenv('EXECUTABLE_PATH'),
                          chrome_options=opt)

# após o login concluído
driver.get("https://www.nuinvest.com.br/configuracoes/relatorios/nota-negociacao")

time.sleep(2)

# seleciona o tipo de ativo para download
span_select_ativo = driver.find_element(By.XPATH, "//span[text()='Selecione o ativo']")
span_select_ativo.click()

span_selected_ativo = driver.find_element(By.XPATH, "//span[text()='B3 - Ações/Opções']")

span_selected_ativo.click()
time.sleep(2)

# seleciona período das notas para download
start_date_picker = driver.find_element(By.XPATH, "//div[@data-test='StartDatePicker']//input[@placeholder='DD/MM/AAAA']")

start_date_picker = driver.find_element(By.XPATH, "//div[@data-test='StartDatePicker']//input[@placeholder='DD/MM/AAAA']")
start_date_picker.clear()
start_date_picker.send_keys("03/07/2023")

time.sleep(2)
end_date_picker = driver.find_element(By.XPATH, "//div[@data-test='EndDatePicker']//input[@placeholder='DD/MM/AAAA']")
end_date_picker.clear()
end_date_picker.send_keys("07/07/2023")

submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

time.sleep(2)

# faz download das notas
tbody = driver.find_element(By.XPATH, "//tbody[@data-test='desktop-body']")
lines = tbody.find_elements(By.TAG_NAME, "tr")

for linha in lines:
    time.sleep(2)
    columns = linha.find_elements(By.TAG_NAME, "td")
    download_element = columns[-1]

    download_element.click()

# driver.quit()
