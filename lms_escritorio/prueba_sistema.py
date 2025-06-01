from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración del WebDriver
driver_path = "C:\\msedgedriver.exe"
service = Service(driver_path)
driver = webdriver.Edge(service=service)
wait = WebDriverWait(driver, 15)

# Datos del nuevo docente
nombre = "Carlos"
apellido = "Ríos"
ci = "654321"  # contraseña
telefono = "12345678"
profesion = "Docente"

try:
    # 1. Iniciar sesión como administrador
    driver.get("http://127.0.0.1:8000/login/")
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.ID, "id_username"))).send_keys("gise")
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.ID, "id_password"))).send_keys("123" + Keys.RETURN)
    time.sleep(2)

    # 2. Ir a la sección de Profesores
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Profesores"))).click()
    time.sleep(2)
    
    # 3. Crear nuevo docente
    driver.get("http://127.0.0.1:8000/docentes/crear/")
    wait.until(EC.presence_of_element_located((By.ID, "nombre"))).send_keys(nombre)
    time.sleep(2)
    driver.find_element(By.ID, "apellido").send_keys(apellido)
    time.sleep(2)
    driver.find_element(By.ID, "ci").send_keys(ci)
    time.sleep(2)
    driver.find_element(By.ID, "telefono").send_keys(telefono)
    time.sleep(2)
    driver.find_element(By.ID, "profesion").send_keys(profesion)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2) 
    
    # 4. Cerrar sesión del admin
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Cerrar sesión"))).click()
    time.sleep(2)

    # 5. Iniciar sesión como docente (usuario = nombre, contraseña = ci)
    driver.get("http://192.168.6.183:8000/docente/login/")
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.ID, "nombre"))).send_keys(nombre)
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.ID, "ci"))).send_keys(ci + Keys.RETURN)
    time.sleep(2)

    # 6. Crear nueva tarea como docente
    wait.until(EC.presence_of_element_located((By.ID, "titulo"))).send_keys("Tarea de prueba")
    time.sleep(2)
    driver.find_element(By.ID, "descripcion").send_keys("Esta es una tarea creada por Selenium.")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(2)

finally:
    driver.quit()
