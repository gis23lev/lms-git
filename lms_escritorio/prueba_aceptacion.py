from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = "C:\\msedgedriver.exe"
service = Service(driver_path)
driver = webdriver.Edge(service=service)
wait = WebDriverWait(driver, 15)

# Datos para crear materia
nombre_materia = "Matemáticas"
codigo_materia = "MAT101"

try:
    # 1. Iniciar sesión (ajusta URL y credenciales)
    driver.get("http://127.0.0.1:8000/login/")
    wait.until(EC.presence_of_element_located((By.ID, "id_username"))).send_keys("gise")
    wait.until(EC.presence_of_element_located((By.ID, "id_password"))).send_keys("123" + Keys.RETURN)
    time.sleep(2)

    # 2. Ir a la página de crear materia
    driver.get("http://127.0.0.1:8000/materias/crear/")
    wait.until(EC.presence_of_element_located((By.ID, "nombre")))
    time.sleep(1)

    # 3. Completar formulario
    driver.find_element(By.ID, "nombre").send_keys(nombre_materia)
    time.sleep(1)
    driver.find_element(By.ID, "codigo").send_keys(codigo_materia)
    time.sleep(1)

    # 4. Enviar formulario
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

finally:
    driver.quit()
