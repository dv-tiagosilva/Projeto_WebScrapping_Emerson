from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Definindo o navegador a se rutilizado: "Chrome"
navegador = webdriver.Chrome()
navegador.implicitly_wait(10)

# acessar o site PaVE - da NCBI
navegador.get("https://pave.niaid.nih.gov/search/search_database")

# colocar o navegador em tela cheia 
navegador.maximize_window()

# selecionar o campo "DataBase" para filtrar a pesquisa selecionando a opção "Genes and regions"
preencher_database = navegador.find_element(By.ID, "region_search")
preencher_database.click()

# selecionar o campo "Select Filters" para clicar em "Host Species"
mover_mouse = navegador.find_element(By.CSS_SELECTOR, 'button[data-bs-target="#collapse-host-filter"]')
actions = ActionChains(navegador)
actions.move_to_element(mover_mouse).perform()  # Move o mouse até o elemento
actions.click().perform()

# esperar (conferir se clicou)
time.sleep(10)

# selecionar a opção "Homo sapiens (Human)" dentro de "Host Species"
# valor="Homo sapiens (Human)"

preencher_host_species = navegador.find_element(By.XPATH, '//input[@value="Homo sapiens (Human)"]')
actions_host_species = ActionChains(navegador)
actions.move_to_element(preencher_host_species).perform()  # Move o mouse até o elemento
actions.click().perform()

# esperar (conferir se clicou)
time.sleep(5)

# preencher o campo "Keyword" com as informações "HPV L1"
preencher_keyword = navegador.find_element(By.ID, "search-inp")
preencher_keyword.send_keys("HPV L1")

# esperar (conferir se digitou "HPV L1" no campo 'Keyword')

# clicar em "GO" para selecionar o que foi digitado no campo "Keyword"
clicar_go = navegador.find_element(By.ID, "keyword_submit")
clicar_go.click()

# esperar (conferir se os filtros foram satisfeitos)
time.sleep(5)

#### agora vou ter que fazer o site clicar em cada link da pesquisa, alterar o tipo de documento para "FACTA" clicar para realizar o download (tentar criar uma função para isso, pois esse método será repetido várias vezes). Após, clicar para voltar para a pagina anterior e clicar no link abaixo do link que foi selecionado, e repetir o processo
'''
# # link_odd = navegador.find_element(By.XPATH, '//*[@id="metadata_table"]/tbody/tr[1]/td[1]/a')
# link_odd = navegador.find_element(By.XPATH, '//td[@class="sorting_1"]/a')

# actions.move_to_element(link_odd).perform()
# actions_link_odd = ActionChains(navegador)
# actions.click().perform()
# time.sleep(10)

# # clicar no typebox "Display Format"
# clicar_format_select = navegador.find_element(By.XPATH, '//*[@id="displayFormatSelect"]')
# clicar_format_select.click()

# # selecionar o formato FASTA
# selecionarFasta = navegador.find_element(By.XPATH, '//*[@id="displayFormatSelect"]/option[3]')
# selecionarFasta.click()

# # clicar nos=vamente no "Display Format" para concluir a seleção do formato FASTA
# clicar_format_select = navegador.find_element(By.XPATH, '//*[@id="displayFormatSelect"]')
# clicar_format_select.click()

# # mover o mouse até o campo de "DOWNLOAD" e clicar no botão
# clicar_download = navegador.find_element(By.XPATH, '//*[@id="downloadFasta"]')
# actions.move_to_element(clicar_download).perform()
# actions_link_download = ActionChains(navegador)
# actions.click().perform()
# time.sleep(10)

# # voltando para página anterior
# navegador.back()
# time.sleep(10)

# # link_odd = navegador.find_element(By.XPATH, '//*[@id="metadata_table"]/tbody/tr[1]/td[1]/a')
'''
actions= ActionChains(navegador)
links = navegador.find_elements(By.XPATH, '//td[@class="sorting_1"]/a')

## Tentar criar isso em uma sequência iterada
for link in links:
    actions.move_to_element(link).perform()
    actions.click().perform()
    time.sleep(10)

    # clicar no typebox "Display Format"
    clicar_format_select = navegador.find_element(By.XPATH, '//*[@id="displayFormatSelect"]')
    clicar_format_select.click()

    # selecionar o formato FASTA
    selecionarFasta = navegador.find_element(By.XPATH, '//*[@id="displayFormatSelect"]/option[3]')
    selecionarFasta.click()

    # clicar nos=vamente no "Display Format" para concluir a seleção do formato FASTA
    clicar_format_select = navegador.find_element(By.XPATH, '//*[@id="displayFormatSelect"]')
    clicar_format_select.click()

    # mover o mouse até o campo de "DOWNLOAD" e clicar no botão
    clicar_download = navegador.find_element(By.XPATH, '//*[@id="downloadFasta"]')
    actions.move_to_element(clicar_download).perform()
    actions_link_download = ActionChains(navegador)
    actions.click().perform()
    time.sleep(10)

    # voltando para página anterior
    navegador.back()
    time.sleep(10)







    
    
    


