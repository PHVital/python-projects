import pyautogui as pg
import time
import pandas as pd

pg.PAUSE = 0.5

pg.press("win")
pg.write("brave")
pg.press("enter")

time.sleep(0.5)
pg.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pg.press("enter")

time.sleep(1)
pg.click(x=435, y=396)
pg.write("emailDeTeste@example.com")
pg.press("tab")
pg.write("senhaforte123")
pg.press("enter")

tabela = pd.read_csv("Aula01\produtos.csv")

for linha in tabela.index:
    pg.click(x=435, y=278)

    codigo = tabela.loc[linha, "codigo"]
    pg.write(str(codigo))
    pg.press("tab")

    marca = tabela.loc[linha, "marca"]
    pg.write(str(marca))
    pg.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pg.write(str(tipo))
    pg.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pg.write(str(categoria))
    pg.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pg.write(str(preco_unitario))
    pg.press("tab")

    custo = tabela.loc[linha, "custo"]
    pg.write(str(custo))
    pg.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pg.write(str(tabela.loc[linha, "obs"]))
    pg.press("enter")

    pg.scroll(5000)