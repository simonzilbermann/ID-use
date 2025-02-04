import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


number_offre=0

# Configurations
TELEGRAM_BOT_TOKEN = "8076057702:AAHZIWauDxm5NP9Aq9ryHM-tyzCfmLZqja0"
TELEGRAM_CHAT_ID = "-4693251247"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, json=payload)


chemin_fichier = os.path.join(os.path.expanduser("~"), "Desktop", "numéros_valides.txt")
chemin_chromedriver = r"C:\Users\user\Desktop\chromedriver.exe"
service = Service(chemin_chromedriver)
driver = webdriver.Chrome(service=service)

with open(chemin_fichier, "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()
        if not ligne:
            continue

        url = f"https://www.shufersal.co.il/couponslp/?ClientID={ligne}"
        print(f"Tentative d'ouvrir : {url}")

        driver.get(url)  # Ouvrir l'URL dans Chrome
        time.sleep(3)  # Attendre le chargement de la page

        try:
            element = driver.find_element(By.XPATH, "//div[@class='title' and contains(text(), 'בקניה בסכום')]")
            if element:
                number_offre += 1
                message = f"✅{number_offre}:  🔎✨An offer was found for id {ligne}✨🔎 \n🔗 {url}"
                send_telegram_message(message)
                print("Message envoyé sur Telegram !")
        except:
            print("❌ Offre non trouvée.")

driver.quit()
