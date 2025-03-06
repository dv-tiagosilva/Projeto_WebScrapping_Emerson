from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

navegador = webdriver.Chrome()

# acessar o site PaVE - da NCBI
navegador.get("https://pave.niaid.nih.gov/search/search_database")

# colocar o navegador em tela cheia 
navegador.maximize_window()


# selecionar o campo "DataBase" para filtrar a pesquisa selecionando a opção "Genes and regions"
preencher_database = navegador.find_element(By.ID, "region_search")
preencher_database.click()

# selecionar o campo "Select Filters" para clicar em "Host Species"
preencher_select_filters = navegador.find_element(By.CSS_SELECTOR, 'button[data-bs-target="#collapse-host-filter"]')
preencher_select_filters.click()

# esperar (conferir se clicou)
time.sleep(10)


# selecionar a opção "Homo sapiens (Human)" dentro de "Host Species"
valor="Homo sapiens (Human)"
preencher_host_species = navegador.find_element(By.XPATH, '//input[@value="Homo sapiens (Human)"]')
preencher_host_species.click()

# esperar (conferir se clicou)
time.sleep(10)

# preencher o campo "Keyword" com as informações "HPV L1"
preencher_keyword = navegador.find_element(By.ID, "search-inp")
preencher_keyword.send_keys("HPV L1")

# esperar (conferir se digitou "HPV L1" no campo 'Keyword')
time.sleep(5)

# clicar em "GO" para selecionar o que foi digitado no campo "Keyword"
clicar_go = navegador.find_element(By.ID, "keyword_submit")
clicar_go.click()

# esperar (conferir se os filtros foram satisfeitos)
time.sleep(10)

# agora vou ter que fazer o site clicar em cada link da pesquisa, alterar o tipo de documento para "FACTA" clicar para realizar o download (tentar criar uma função para isso, pois esse método será repetido várias vezes). Após, clicar para voltar para a pagina anterior e clicar no link abaixo do link que foi selecionado, e repetir o processo







