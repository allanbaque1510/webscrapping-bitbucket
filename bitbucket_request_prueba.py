from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import xlsxwriter

# Pedir al usuario que ingrese la URL
url = input("Ingresa la URL de Bitbucket del commit para obtener la documentacion: ")

# Configurar driver Edge con webdriver-manager
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

# Configurar cookies
cookies = {
    "JSESSIONID": "",
    "__cuid": "",
    "ajs_anonymous_id": "",
    "atl-bsc-consent-token": "",
    "atl-bsc-show-banner": "",
    "bb_session": "",
    "cloud.session.token": "",
    "csrftoken": ""
}

# Navegar a dominio para setear cookies
driver.get("https://bitbucket.org")

for name, value in cookies.items():
    driver.add_cookie({"name": name, "value": value})

driver.get(url)

# Esperar que la página cargue
try:
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".commit-details"))
    )
except:
    print("No se encontró el elemento o se agotó el tiempo")

# AQUI SE OBTUVO YA EL HTML, SE PROCEDE A OBTENER LA INFRMACION
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
data = []
contenido = soup.find_all("div", class_="css-2mk060 e1sanmi10")
servidor = soup.find("div", class_="css-1oagmxp").find("div",class_="css-5mhfd2").find("h2").find("div").text
for divs in contenido:
   ruta = divs.find('div', class_="css-15ur4lm e1sanmi11")['id'].replace("chg-", "")
   rutaFinal = url + "#" + ruta
   directorio, archivo = ruta.rsplit("/", 1)
   data.append((directorio, archivo, rutaFinal))

driver.quit()


workbook = xlsxwriter.Workbook('documentacion bitbucket.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'servidor')
worksheet.write('B1', 'Aplicacion')
worksheet.write('C1', 'directorio')
worksheet.write('D1', 'archivo')
worksheet.write('E1', 'link')

for row_num, (directorio, archivo,rutaFinal) in enumerate(data, start=1):
    worksheet.write_url(row_num, 0, 'https://bitbucket.org/servidor/src/master/', string='proyecto')
    worksheet.write(row_num, 1, servidor)
    worksheet.write(row_num, 2, directorio)
    worksheet.write(row_num, 3, archivo)
    worksheet.write_url(row_num, 4, rutaFinal, string='link')
workbook.close()

