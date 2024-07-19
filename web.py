from selenium import webdriver   #acessar website
from selenium.webdriver.common.by import By   #para especificar tipo de elemento procurado
# import os  #especificar pastas e local de arquivos no note
# from pathlib import Path  #infelizmente não funcionou corretamente, descartar opção
# import time  #implementar pausas entre os códigos
# from selenium.webdriver.common.keys import Keys  #selecionar tecla do teclado



# driver = webdriver.Chrome()  #padrão
# site = driver.get("https://www.alura.com.br/")  #site escolhido

## Encontrar elemento 'ID' no site através do 'id=header...' ao inspecionar site
# local = driver.find_element(By.ID, "header-barraBusca-form-campoBusca")
# local.send_keys('Vamos chegar lá')  #preencher campo digitável do site

## Encontrar elemento 'CLASS NAME' no site através do 'class=header...' ao inspecionar site
# driver.find_element(By.CLASS_NAME, "header__nav--ctas-matricule").click()
# time.sleep(10) 

## Encontrar elemento 'TAG_NAME' no site através da tag exibido ao inspecionar site (tags ex. = (a, /a), (html, /html), (body, /body))
# texto = driver.find_element(By.TAG_NAME, 'h1').text
# print(texto)
 
## Encontrar elemento 'XPATH'(caminho) para localizar logos, imagens ao inspecionar e copiar o xpath
# logo = driver.find_element(By.XPATH, "/html/body/main/section[1]/header/div/nav/a/img").click()

## Encontrar elemento 'PARTIAL_LINK_TEXT' no site através de um nome exibido na página, desde que seja link
# find = driver.find_element(By.PARTIAL_LINK_TEXT, 'corporativa').text
# print(find)

## Encontrar elemento 'NAME' no site através do 'name=curso...' exibido ao inspecionar site
# name = driver.find_element(By.NAME, 'curso HTML').click()

## Encontrar elemento específico percorrendo classe e buscando seu nome
# teste = driver.find_elements(By.CLASS_NAME, 'header__nav--menu')
# for elemento in teste:
#     if 'como' in elemento.text.lower() or 'funciona' in elemento.text.lower():
#         elemento.click()
#         break

## Especificar atributo desejado para encontrar links, clicks, texts mais precisamente
# texto = driver.find_element(By.XPATH, "/html/body/main/section[1]/header/div/nav/div[4]/a[1]").get_attribute('href')
# print(texto)

## Encontrar elementos dentro de tags dentro de classes
# qtd = driver.find_elements(By.CLASS_NAME, 'homeDestaqueDepoimentos--item-body-preview')
# for elemento in qtd:
#     busca2 = elemento.find_element(By.TAG_NAME, 'a').get_attribute('href')
#     print(busca2)


## EXERCICIO I

# local = os.getcwd()  #encontrar local do arquivo html
# arquivo = local + r"\formulario.html"  #local + nome do arquivo
# driver.get(arquivo)  #para o driver acessar nosso arquivo
# driver.find_element(By.XPATH, '/html/body/form/input[1]').click()  #clicar no local selecionado
# time.sleep(1)

# alerta = driver.switch_to.alert  #reconhecer mensagem de alerta ao aparecer
# alerta.accept()  #aceitar mensagem (OK)
# time.sleep(1)

# driver.find_element(By.XPATH, "/html/body/form/input[3]").click()  #clicar no botão para marcá-lo
# time.sleep(1)
# driver.find_element(By.XPATH, "/html/body/form/input[3]").click()  #clicar para desmarcar
# time.sleep(1)

# tellme = driver.find_element(By.XPATH, "/html/body/form/input[3]").is_selected()  #verificar se botão está selecionado
# print(tellme)

# driver.find_element(By.XPATH, '/html/body/form/input[4]').send_keys('#E82121')
# time.sleep(1)  #alterar a cor

# driver.find_element(By.XPATH, '/html/body/form/input[5]').send_keys('#2143E8')
# time.sleep(1)  #alterar a cor

# driver.find_element(By.XPATH, '/html/body/form/input[6]').send_keys('10/02/2000')
# time.sleep(1)  #selecionar a data 

# from selenium.webdriver.common.keys import Keys  #selecionar tecla do teclado
# driver.find_element(By.XPATH, '/html/body/form/input[7]').send_keys('27/02/2003', Keys.TAB, '17:20' )
# time.sleep(1)  #selecionar a data e horário

# driver.find_element(By.XPATH, '/html/body/form/input[8]').send_keys(r'C:\Users\leand\OneDrive\Documentos\hashtag\formulario.html')
# time.sleep(1)  #anexar arquivo

# valor = driver.find_element(By.XPATH, '/html/body/form/input[9]').send_keys('julho', Keys.TAB, '1975')
# time.sleep(1)  #selecionar mês e ano

# driver.find_element(By.XPATH, '/html/body/form/input[10]').send_keys('17')
# time.sleep(1) #digitar números

# driver.find_element(By.XPATH, '/html/body/form/input[11]').send_keys('debugger')
# time.sleep(1)  #digitar senha

# driver.find_element(By.XPATH, '/html/body/form/input[13]').click()
# time.sleep(1)  #selecionar botão do meio

# for i in range(70 - 50):  #mover barra até o 70
#     driver.find_element(By.XPATH, '/html/body/form/input[15]').send_keys(Keys.ARROW_RIGHT)
# time.sleep(1)  

# driver.find_element(By.XPATH, '/html/body/form/input[16]').send_keys('Flamengo')
# time.sleep(1)  #digitar dentro do quadro

# driver.find_element(By.XPATH, '/html/body/form/input[17]').send_keys('10:25')
# time.sleep(1)  #definir horário

# driver.find_element(By.XPATH, '/html/body/form/input[18]').send_keys('17' , '2010')
# time.sleep(1)  #definir semana e ano

# driver.find_element(By.XPATH, '//*[@id="story"]').send_keys('Que honra, Leandro!',Keys.ENTER, 'Mais uma vitória.',Keys.ENTER, 'Estou orgulhoso!')
# time.sleep(1)  #digitar textos maiores

# driver.find_element(By.XPATH, '//*[@id="story"]').clear()
# time.sleep(1)  #limpar todo texto digitado

## 2 Formas de selecionar uma caixa de opções
# driver.find_element(By.XPATH, '/html/body/form/select[1]').send_keys('A')
# time.sleep(1)
##Ou
# from selenium.webdriver.support.select import Select  #importar novas ferramentas select
# caixa = driver.find_element(By.TAG_NAME, 'select')  #salvar em variável o local pelo nome da tag
# caixa_select = Select(caixa)  #ativar função select
# caixa_select.select_by_index('1')  #selecionar index (entre várias outras opções)
# time.sleep(1)
# caixa_select.deselect_all()  #remover seleção


## EXERCICIO II

# from selenium import webdriver   #acessar website
# from selenium.webdriver.common.by import By   #para especificar tipo de elemento procurado
# import os #especificar pastas e local de arquivos no note
# # from pathlib import Path  #infelizmente não funcionou corretamente, descartar opção
# import time  #implementar pausas entre os códigos
# from selenium.webdriver.common.keys import Keys  #selecionar tecla do teclado
# from openpyxl import Workbook, load_workbook  #interagir com planilhas excel

# wb = load_workbook('NotasEmitir.xlsx')  #carregar sheet
# ws = wb.active  #code padrão para ativar funcionalidade

# lista = list(ws.values)  #acess values row by row and put into list
# lista.remove(lista[0])   #remove first row from sheet

## ativar chrome e acessar our archive
# driver = webdriver.Chrome()
# local = os.getcwd()   
# arquivo = local + '\login.html'  
# driver.get(arquivo)

# driver.find_element(By.XPATH, '/html/body/div/form/input[1]').send_keys('Leandro', Keys.TAB )
# time.sleep(0.5)
# driver.find_element(By.XPATH, '/html/body/div/form/input[2]').send_keys('1710', Keys.ENTER)
# time.sleep(1)  #login sucessfull

# for elemento in lista:
#     cliente, cpf, cep, endereço, bairro, municipio, uf, inscrição, descrição, quantidade, valor_uni, valor_total = elemento
#     driver.find_element(By.XPATH, '//*[@id="nome"]').send_keys(cliente)
#     time.sleep(0.5)
#     driver.find_element(By.NAME, 'endereco').send_keys(endereço)
#     time.sleep(0.5)
#     driver.find_element(By.NAME, 'bairro').send_keys(bairro)
#     time.sleep(0.5)
#     driver.find_element(By.NAME, 'municipio').send_keys(municipio)
#     time.sleep(0.5)
#     driver.find_element(By.NAME, 'cep').send_keys(cep)
#     time.sleep(0.5)
#     driver.find_element(By.NAME, 'uf').send_keys(uf)
#     time.sleep(0.5)
#     driver.find_element(By.NAME, 'cnpj').send_keys(cpf)
#     time.sleep(0.5)
#     driver.find_element(By.NAME, 'inscricao').send_keys(inscrição)
#     time.sleep(0.5)
#     driver.find_element(By.NAME, 'descricao').send_keys(descrição)
#     time.sleep(0.5)
#     driver.find_element(By.NAME, 'quantidade').send_keys(quantidade)
#     time.sleep(0.5)
#     driver.find_element(By.NAME, 'valor_unitario').send_keys(valor_uni)
#     time.sleep(0.5)
#     driver.find_element(By.NAME, 'total').send_keys(valor_total)
#     time.sleep(0.5)
#     driver.find_element(By.XPATH, '//*[@id="formulario"]/button').click()
#     time.sleep(0.5)
    
#     driver.refresh()  #recarregar a página para zerar o formulário

## GABARITO FEITO COM PANDAS

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_experimental_option("prefs", {
#   "download.default_directory": r"C:\Users\joaol\downloads",
#   "download.prompt_for_download": False,
#   "download.directory_upgrade": True,
#   "safebrowsing.enabled": True
# })

# servico = Service(ChromeDriverManager().install())
# navegador = webdriver.Chrome(service=servico, options=options)

# # entrar na página de login (no nosso caso é login.html)
# import os

# caminho = os.getcwd()
# arquivo = caminho + r"\login.html"
# navegador.get(arquivo)

# # preencher o login e a senha
# navegador.find_element(By.XPATH, '/html/body/div/form/input[1]').send_keys("lira@gmail.com")
# navegador.find_element(By.XPATH, '/html/body/div/form/input[2]').send_keys("123456")
# # clicar no botao de fazer login
# navegador.find_element(By.XPATH, '/html/body/div/form/button').click()
# # importar a base de clientes
# import pandas as pd

# tabela = pd.read_excel("NotasEmitir.xlsx") 
# print(tabela)

# # para cada cliente - rodar o processo de emissao de nota fiscal
# for linha in tabela.index:

#     # preencher os dados da NF

#     navegador.find_element(By.NAME, 'nome').send_keys(tabela.loc[linha, "Cliente"])
#     navegador.find_element(By.NAME, 'endereco').send_keys(tabela.loc[linha, "Endereço"])
#     navegador.find_element(By.NAME, 'bairro').send_keys(tabela.loc[linha, "Bairro"])
#     navegador.find_element(By.NAME, 'municipio').send_keys(tabela.loc[linha, "Municipio"])
#     navegador.find_element(By.NAME, 'cep').send_keys(str(tabela.loc[linha, "CEP"]))
#     navegador.find_element(By.NAME, 'uf').send_keys(tabela.loc[linha, "UF"])
#     navegador.find_element(By.NAME, 'cnpj').send_keys(str(tabela.loc[linha, "CPF/CNPJ"]))
#     navegador.find_element(By.NAME, 'inscricao').send_keys(str(tabela.loc[linha, "Inscricao Estadual"]))
#     texto = tabela.loc[linha, "Descrição"]
#     navegador.find_element(By.NAME, 'descricao').send_keys(texto)
#     navegador.find_element(By.NAME, 'quantidade').send_keys(str(tabela.loc[linha, "Quantidade"]))
#     navegador.find_element(By.NAME, 'valor_unitario').send_keys(str(tabela.loc[linha, "Valor Unitario"]))
#     navegador.find_element(By.NAME, 'total').send_keys(str(tabela.loc[linha, "Valor Total"]))
#     navegador.find_element(By.CLASS_NAME, 'registerbtn').click()  # clicar em emitir nota fiscal
#    
#     navegador.refresh()  # recarregar a página para limpar o formulário
#     navegador.quit()  # encerrar navegador


##Interagir com pop-ups (alertas)

## forma simples
# alerta = driver.switch_to.alert
# alerta.accept()

## forma "completa"
# from selenium.webdriver.common.alert import Alert
# alerta = Alert(driver)
# alerta.accept() 
## ou
# alerta.dismiss()  #para cancelar

## acessar texto do pop-up
# alerta = Alert(driver)
# texto = alerta.text
# print(texto)

## pop-up de input
# lerta = driver.switch_to.alert
# time.sleep(2)
# alerta.send_keys('123123') # lembre que ele funciona, apesar de não aparecer
# alerta.accept()

## Novas ferramentas úteis para simular ações do mouse
# from selenium.webdriver import ActionChains

# menu = driver.find_element(By.XPATH, '//*[@id="menu-item-dropdown-16313"]')
# item = driver.find_element(By.XPATH, '//*[@id="menu-item-17042"]/a')

# ActionChains(driver).move_to_element(menu).perform()  #colocar o mouse em cima do menu

# item.click()  # clicar no item

## Alternar entre abas (selenium reconhece uma por vez)
# print(driver.window_handles)  #visualizar todas as abas abertas
# aba_original = driver.window_handles[0]  #salvar primeira aba em variável
# nova_aba = driver.window_handles[1]  #salva segunda aba em variável
# driver.switch_to.window(nova_aba)  #selecionar nova aba para interações

# ## Visualizar títulos das abas abertas
# for aba in driver.window_handles:
#     driver.switch_to.window(aba)
#     print(driver.title)

# driver.close() #fecha a aba selecionada no momento

# # Verificar se elemento já carregou/exibiu - Forma 1 
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# driver.get("https://hashtagtreinamentos.com")

# elemento = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'use')))
# time.sleep(1)
# elemento.click()

# Verificar se elemento já carregou/exibiu - Forma 2 (elemento web não coincide com len(), incorreto)
# while len(driver.find_element(By.TAG_NAME,'use')) == 0:
#     time.sleep(1)

# driver.find_element(By.TAG_NAME, 'use').click()
# time.sleep(0.5)


## EXERCICIO III - PROCESSO JURÍDICO
# from selenium import webdriver  #web
# from selenium.webdriver.common.by import By   #find
# from selenium.webdriver.common.keys import Keys  #selecionar teclas
# from selenium.webdriver import ActionChains  #simulador mouse
# import os  #local archive
# import time  #sleep
# import pyautogui

# ## Localizar arquivo 
# local = os.getcwd()
# arquivo = local + '/index3.html'
# driver.get(arquivo)


# drop_menu = driver.find_element(By.CLASS_NAME, 'dropdown-menu')  #find element in the page
# move = ActionChains(driver).move_to_element(drop_menu).perform()  #move mouse to element
# driver.find_element(By.XPATH, '/html/body/div/div/div/a[2]').click()  #click in above element select

# aba_orig = driver.window_handles[0] #aba original
# nova_aba = driver.window_handles[1] #aba nova

# driver.switch_to.window(nova_aba)  #change focus to new aba
# time.sleep(1)
# driver.find_element(By.ID, 'nome').send_keys('Leandro')
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.press('enter')
# time.sleep(0.5)

# pop_up = driver.switch_to.alert  #accept popup
# time.sleep(0.5)
# pop_up.accept()
# time.sleep(7)

# while True:  apenas continuar o código se alerta for encontrado
#     try:
#         alerta = driver.switch_to.alert
#         break   
#     except:
#         time.sleep(1.5)

# alerta2 = driver.switch_to.alert.text
# if 'Processo encontrado com sucesso!' in alerta2:
#     print('Deu certo')
#     alerta.accept()
# else:
#     print('Processo não encontrado')
#     alerta.accept()


## EXERCICIO IV - Automatizar tabela Processos

# from selenium import webdriver
# import pandas as pd
# import os
# from selenium.webdriver import ActionChains
# from time import sleep

# # selecionar arquivo web
# driver = webdriver.Chrome()
# local = os.getcwd()
# archive = local + '/index3.html'

# # carregar planilha
# sheet = pd.read_excel('Processos.xlsx')
# print(sheet)

# # preencher formulario com dados da planilha
# for index in sheet.index:
#     nome = sheet.loc[index, 'Nome']
#     advogado = sheet.loc[index, 'Advogado']
#     processo = sheet.loc[index, 'Processo']
#     cidade = sheet.loc[index, 'Cidade']

#     driver.get(archive)

#     drop_menu = driver.find_element(By.CLASS_NAME, 'dropdown-menu')  #find element in the page
#     move = ActionChains(driver).move_to_element(drop_menu).perform()  #move mouse to element
#     if cidade == 'Distrito Federal':
#         driver.find_element(By.XPATH, '/html/body/div/div/div/a[1]').click()
#     elif cidade == ' Rio de Janeiro':
#         driver.find_element(By.XPATH, '/html/body/div/div/div/a[2]').click()
#     else:
#         driver.find_element(By.XPATH, '/html/body/div/div/div/a[3]').click()

#     indice = index + 1 
#     newaba = driver.window_handles[indice]    
#     driver.switch_to.window(newaba)

#     driver.find_element(By.ID, 'nome').send_keys(nome)
#     driver.find_element(By.ID, 'advogado').send_keys(advogado)
#     driver.find_element(By.ID, 'numero').send_keys(processo)
#     driver.find_element(By.CLASS_NAME,'registerbtn').click()
#     # sleep(1)
#     alerta = driver.switch_to.alert
#     alerta.accept()
    
#     while True:
#         try:
#             alerta2 = driver.switch_to.alert
#             break
#         except:
#             sleep(1)
        
#     if 'Nenhum processo encontrado!' in alerta2.text:
#         sheet.loc[index, 'Status'] = 'Encontrado'
#     else:
#        sheet.loc[index, 'Status'] = 'Não encontrado'
    
#     origin = driver.window_handles[0]
#     driver.switch_to.window(origin)

# print(sheet)
# driver.quit()
# print('Finish!')


## Retornar uma lista de pelo menos 50 vídeos de Python no Youtube

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome()
# driver.get("https://youtube.com")

# driver.find_element(By.NAME, "search_query").send_keys("python")
# driver.find_element(By.NAME, "search_query").send_keys(Keys.ENTER)
# time.sleep(2)

# # dar um scroll (rolamento pra baixo) na página
# for i in range(15):  #15 rolamentos
#     scroll = 4000 * i   #rolar scroll equivalente a 4000
#     driver.execute_script(f"window.scroll(0, {scroll});")  #executar comando em java(x , y) (x = barra horizontal e y = vertical)
#     time.sleep(2)

#     #encontrar lista de elementos 'thumbnail'
#     lista_videos = driver.find_elements(By.ID, "thumbnail")

# #percorrer lista e encontrar o atributo de cada um elemento da lista
# for video in lista_videos:
#     print(video.get_attribute("href"))


## Retornar texto da data do jogo mandante da 1ª linha da tabela

# from selenium import webdriver
# import time

# link = "https://pbdatatrader.com.br/jogosdodia"
# driver = webdriver.Chrome()
# driver.get(link)
# time.sleep(7)

# iframe = driver.find_element(By.TAG_NAME, "iframe")  #encontrar tag iframe no começo da inspeção, que abrange todo o conjunto que também abrange o frame desejado
# driver.switch_to.frame(iframe)  #mudar foco do selenium para o conjunto selecionado

# iframe = driver.find_element(By.TAG_NAME, "iframe")   #com foco no conjunto selecionado, encontrar o iframe onde está o frame desejado
# driver.switch_to.frame(iframe)  #finalmente mudar o foco para o frame desejado

# texto = driver.find_element(By.XPATH, '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[19]/transform/div/div[3]/div/div/visual-modern/div/div/div[2]/div[1]/div[2]/div/div[2]/div/div/div[2]')
# print(texto.text)  #exibir texto do caminho do frame


## EXERCICIO V - Retornar valores de uma tabela web, formatar e transformar em DataFrame

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd


link = "https://pbdatatrader.com.br/jogosdodia"
driver = webdriver.Chrome()
driver.get(link)

while True:
    sleep(3)
    try:
        iframe1 = driver.find_element(By.TAG_NAME, 'iframe')    
        driver.switch_to.frame(iframe1)
        break
    except:
        sleep(0.5)

iframe1 = driver.find_element(By.TAG_NAME, 'iframe')
driver.switch_to.frame(iframe1)

tabela = driver.find_element(By.XPATH, '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[19]/transform/div/div[3]/div/div/visual-modern/div/div/div[2]/div[1]')

texto = tabela.text
lista = texto.split('\n')
tabela_format = [item for item in lista if item not in ['Seleção de Linha', 'Selecionar Linha']]

colunas = tabela_format[:10]
valores = tabela_format[10:]

dicio_colums = {coluna: [] for coluna in colunas}

for i in range(0, len(valores), 10):
    row = valores[i : i + 10]
    if len(row) == 10:
        for coluna, linha in zip(colunas, row):
            dicio_colums[coluna].append(linha)
# print(dicio_colums)  

# for chave, valor in dicio_colums.items():
#     print(f'{chave}:{valor}')

df = pd.DataFrame.from_dict(dicio_colums)
print(df)