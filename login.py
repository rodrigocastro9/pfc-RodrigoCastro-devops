import time #para el tiempo de espera
# import outlook
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("http://localhost:80")
elemento1 = driver.find_element(By.ID, "user")
elemento1.clear()
elemento1.send_keys("root")
time.sleep(2)
elemento2 = driver.find_element(By.NAME, "pass")
elemento2.clear()
elemento2.send_keys("password")
time.sleep(2)
driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click()

element=driver.find_element(By.XPATH, "//span[@class='left'][contains(.,'Creación rápida de ticket')]")

#Verificamos estar en la card de crear ticket
if element.is_displayed():
    print("Nos encontramos en el card de ticker")
else : 
    print("Error al llegar al index" + driver.close())

asunto=driver.find_element(By.XPATH,"(//input[@name='Subject'])[3]")
asunto.clear()
asunto.send_keys("Esto es un asunto para el parical")
time.sleep(1)
contenido=driver.find_element(By.XPATH,"//textarea[contains(@name,'Content')]")
contenido.clear()
contenido.send_keys("Contenido para la prueba")
time.sleep(1)
#Hacemos clicl en el elemento
driver.find_element(By.XPATH, "//input[@value='Crear']").click()

time.sleep(15)

driver.close()

