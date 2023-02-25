import sqlite3
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



conexao = sqlite3.connect('crawlers.sqlite3')
cursor = conexao.cursor()
sql = 'insert into noticia (categoria, titulo, data, descricao) values (?,?,?,?)'


navegador = Chrome(service=Service(ChromeDriverManager().install()))
navegador.get("https://raspagem.herokuapp.com/noticias/")



links = navegador.find_element(By.CSS_SELECTOR, 'ul.nav.nav-pills').text
links = links.split('\n')
for link in links:
    a = navegador.find_element(By.LINK_TEXT, link)
    a.click()
    for noticia in navegador.find_elements(By.CSS_SELECTOR, 'div.position-static'):
        titulo = noticia.find_element(By.TAG_NAME, 'h3').text
        data = noticia.find_element(By.CSS_SELECTOR,'div.text-muted').text
        descricao = noticia.find_element(By.TAG_NAME,'p').text
        valores = [link, titulo, data, descricao]
        cursor.execute(sql,valores)
navegador.close()
conexao.commit()
conexao.close()