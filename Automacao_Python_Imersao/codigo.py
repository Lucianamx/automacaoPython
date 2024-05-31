#Passo a passo de construção

#Passo 1 Entrar no sistema https://dlp.hashtagtreinamentos.com/python/intensivao/login
# depois de instalada caso ainda não tenha feito importamos a  a biblioteca que vai permitir com 
#que você controle o mouse e o seuteclado para fazer as automações no seu computador utilizando o Python.
import pyautogui
import time
import pandas as pd
#Para dar um intervalo a cada  PAUSE
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "l") 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
#time.sleep(3)

#Passo 2 login
pyautogui.click(x=397, y=408)
pyautogui.write("lmx@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")

#Passo 3 Importar os produtos a serem cadastrados necessario pandas
produtos = pd.read_csv("produtos.csv")
#passo 4 cadastrar os produtos
#For para cada linha da tabela ser cadastrada ele ja começa no indice 0
for linha in produtos.index:
    # clicar no campo de código
    pyautogui.click(x=389, y=295)
    # pegar da tabela o valor do campo que a gente quer preencher loc significa localização
    codigo = produtos.loc[linha, "codigo"]
    # preencher o campo (str para tranforamr tudo em string)
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo/ para simplificar transformando tudo em uma linha
    pyautogui.write(str(produtos.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(produtos.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(produtos.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(produtos.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(produtos.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = produtos.loc[linha, "obs"]
    #valida se o campo está vazio
    if not pd.isna(obs):
        pyautogui.write(str(produtos.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

#Repetir o processo até o final da lista