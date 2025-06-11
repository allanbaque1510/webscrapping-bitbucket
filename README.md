# 📄 Proyecto de Web Scraping Bitbucket + Exportación a Excel

Este proyecto realiza un **Web Scraping** de Bitbucket para obtener datos específicos de una URL de *commit*, utilizando **Selenium**, **BeautifulSoup** y exportando los resultados a un archivo **Excel (.xlsx)** con formato.

---

## 🚀 ¿Qué hace este script?

1. Pide al usuario ingresar una URL de Bitbucket.
2. Usa Selenium para abrir el navegador Edge y acceder a esa URL.
3. Extrae datos de HTML usando **BeautifulSoup**.
4. Procesa los datos para separar rutas de archivos modificados:
   - Directorio principal.
   - Nombre del archivo.
   - Enlace al archivo (`url`).
5. Exporta los resultados a un archivo de Excel, donde:
   - Las columnas incluyen: repositorio, servidor, directorio, archivos y enlaces.
   - Se formatean los archivos en una lista y los links como hipervínculos.

---

## 🧰 Tecnologías utilizadas

- Python 3.10+
- Selenium
- BeautifulSoup4
- Webdriver Manager (Edge)
- XlsxWriter

---

## 📷 Capturas del proceso

### 🖥️ Entrada: URL proporcionada por el usuario

![Ingreso URL](img/url-input.png)

---

### 🌐 Navegación automática con Selenium

![Selenium ejecutando Edge](img/selenium.png)

---

### 📊 Salida en Excel con hipervínculos y agrupación por directorio

![Excel con resultados](img/excel.png)

---

## 📁 Estructura de salida

| Repositorio         | Servidor | Directorio             | Archivos           | Links                  |
|---------------------|----------|------------------------|--------------------|-------------------------|
| proyecto            | PROD     | `app/Helpers`          | helper.php         | [link](#)               |
| proyecto            | PROD     | `app/Http/Controllers` | BaseController.php | [link](#) |

---

## 🧪 Cómo usar

1. Instala los paquetes necesarios:

```bash
pip install selenium beautifulsoup4 xlsxwriter webdriver-manager
```
2. Asegúrate de tener Microsoft Edge instalado en tu sistema.
3. Modifica el script e ingresa las cookies de acceso de tu cuenta bitbucket, y la url de tu proyecto.
4. Ejecuta el script:
```bash
python bitbucket_request_prueba.py
```
5. Cuando el programa lo solicite, ingresa una URL válida de un commit de Bitbucket.

6. El navegador Edge se abrirá automáticamente, navegará a la URL, extraerá los datos y generará un archivo llamado:
**documentacion bitbucket.xlsx**
7. Abre el archivo Excel generado para ver los resultados agrupados por directorio, con los nombres de archivos y enlaces de acceso directo.

