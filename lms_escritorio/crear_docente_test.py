from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura la ruta del driver (ajusta según tu EdgeDriver)
driver_path = "C:\\msedgedriver.exe"
service = Service(driver_path)

driver = webdriver.Edge(service=service)
wait = WebDriverWait(driver, 10)  # Espera explícita hasta 10 segundos

try:
    # 1. Ir a la página de login
    driver.get("http://127.0.0.1:8000/login/")  # Cambia la URL según tu proyecto
    
    
    # Esperar que cargue
    time.sleep(2)
    
    
    # 2. Esperar y completar usuario y contraseña
    username = wait.until(EC.presence_of_element_located((By.ID, "id_username")))
    username.send_keys("gise")
    time.sleep(2)

    password = wait.until(EC.presence_of_element_located((By.ID, "id_password")))
    password.send_keys("123")
    password.send_keys(Keys.RETURN)
    time.sleep(2)

    # 3. Esperar que cargue el dashboard (ejemplo, espera que aparezca el enlace "Profesores")
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Profesores")))
    time.sleep(2)

    # 4. Navegar a la sección "Profesores"
    driver.find_element(By.LINK_TEXT, "Profesores").click()
    time.sleep(2)

    # 5. Esperar a que cargue la página de Profesores
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(2)
    

    # 6. Ir a la página de crear docente (puedes cambiar por clic si tienes botón)
    driver.get("http://127.0.0.1:8000/docentes/crear/")
    time.sleep(2)

    # 7. Esperar que cargue el formulario
    wait.until(EC.presence_of_element_located((By.ID, "nombre")))

    # 8. Completar el formulario
    driver.find_element(By.ID, "nombre").send_keys("Juan")
    time.sleep(2)
    driver.find_element(By.ID, "apellido").send_keys("Pérez")
    time.sleep(2)
    driver.find_element(By.ID, "ci").send_keys("159753")
    time.sleep(2)
    driver.find_element(By.ID, "telefono").send_keys("78945612")
    time.sleep(2)
    driver.find_element(By.ID, "profesion").send_keys("Ingeniero")
    time.sleep(2)

    # 9. Enviar el formulario
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)


    # 10. Esperar un poco para ver resultado (puedes ajustar esto)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

finally:
    time.sleep(2)

    driver.quit()
