from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

# Ruta al ejecutable de EdgeDriver (ajústala según dónde lo guardaste)
driver_path = "C:\\msedgedriver.exe"
service = Service(driver_path)

# Iniciar el navegador Edge
driver = webdriver.Edge(service=service)

# Abre la página de login
driver.get("http:/127.0.0.1:8000/login") # Cambia esto

# Esperar que cargue
time.sleep(2)

# Completar campos
driver.find_element(By.ID, "id_username").send_keys("gise")
time.sleep(2)
driver.find_element(By.ID, "id_password").send_keys("123")
time.sleep(2)

# Enviar el formulario
driver.find_element(By.TAG_NAME, "form").submit()

# Esperar unos segundos para ver el resultado
time.sleep(15)

# Cerrar el navegador
driver.quit()
