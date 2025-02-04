import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chemin_fichier = os.path.join(os.path.expanduser("~"), "Desktop", "israelim.txt")
nouveau_fichier = os.path.join(os.path.expanduser("~"), "Desktop", "numéros_valides.txt")  # Nouveau fichier

# Spécifier le chemin du ChromeDriver local
chemin_chromedriver = r"C:\Users\user\Desktop\chromedriver.exe"
service = Service(chemin_chromedriver)

# Lancer Chrome en mode automatisé avec le chemin spécifié
driver = webdriver.Chrome(service=service)

id_touver=0
data_base_ligne=0

# Ouvrir le fichier pour écrire les numéros valides
with open(nouveau_fichier, "w", encoding="utf-8") as fichier_sortie:
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        for _ in range(5):  # Ignorer les 5 premières lignes#(11421) (4772)
            f.readline()

        # Traiter toutes les lignes restantes
        for ligne in f:
            ligne = ligne.strip()
            if not ligne:
                continue

            valeurs = ligne.split(",")  # Séparer les valeurs par virgule
            if len(valeurs) > 3:  # Vérifier si la 4ème valeur existe
                client_id = valeurs[3].strip("'")  # Extraire et nettoyer le numéro
                url = f"https://www.shufersal.co.il/couponslp/?ClientID={client_id}"
                data_base_ligne+=1
                print(f"({data_base_ligne})|  Tentative d'ouvrir : {url}")

                driver.get(url)  # Ouvrir l'URL dans Chrome

                # Attendre que la page se charge (attendre jusqu'à 5 secondes)
                time.sleep(3)

                try:
                    # Vérifier si le message "לא נמצאו קופונים להצגה" est présent
                    message = driver.find_element(By.XPATH, "//*[contains(text(),'לא נמצאו קופונים להצגה')]")
                    print(f"Message trouvé sur : {url}, mais on continue.")
                except:
                    # Si le message n'est pas trouvé, on écrit le client_id dans le fichier
                    fichier_sortie.write(client_id + "\n")
                    id_touver += 1
                    print(f"({id_touver})|  Page avec coupons trouvée, numéro ajouté : {client_id}")

                time.sleep(1)  # Attendre 10 secondes avant d'ouvrir la suivante

driver.quit()  # Fermer le navigateur une fois terminé
