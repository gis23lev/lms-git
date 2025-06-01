from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Ruta del EdgeDriver
driver_path = "C:\\msedgedriver.exe"
service = Service(driver_path)
driver = webdriver.Edge(service=service)
wait = WebDriverWait(driver, 20)

try:
    # 1. Login
    driver.get("http://127.0.0.1:8000/login/")
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.ID, "id_username"))).send_keys("gise")
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.ID, "id_password"))).send_keys("123" + Keys.RETURN)
    time.sleep(2)

    # 2. Ir a Profesores
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Profesores"))).click()
    time.sleep(2)


    # 3. Crear Docente
    driver.get("http://127.0.0.1:8000/docentes/crear/")
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.ID, "nombre"))).send_keys("Juan")
    time.sleep(2)
    driver.find_element(By.ID, "apellido").send_keys("Pérez")
    time.sleep(2)
    driver.find_element(By.ID, "ci").send_keys("159753")
    time.sleep(2)
    driver.find_element(By.ID, "telefono").send_keys("78945612")
    time.sleep(2)
    driver.find_element(By.ID, "profesion").send_keys("Ingeniero")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    # 4. Volver a Profesores
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Profesores"))).click()
    time.sleep(2)

    # 5. Buscar el docente creado y hacer clic en "Editar"
    wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Juan')]/following-sibling::td/a[contains(text(),'Editar')]"))).click()
    time.sleep(2)

    # 6. Editar el campo Profesión
    profesion_field = wait.until(EC.presence_of_element_located((By.ID, "profesion")))
    time.sleep(2)
    profesion_field.clear()
    time.sleep(2)
    profesion_field.send_keys("Arquitecto")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)


    # 7. Volver a Profesores
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Profesores"))).click()

    # 8. Buscar el docente y hacer clic en "Eliminar"
    wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Juan')]/following-sibling::td/a[contains(text(),'Eliminar')]"))).click()
    time.sleep(2)


finally:
    time.sleep(2)
    driver.quit()
