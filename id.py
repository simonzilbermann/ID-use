from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Définir le nombre d'itérations (mettre None pour une boucle infinie)
nb_iterations = 50  # Mettre None pour une boucle infinie

# Démarrer la boucle
iteration = 0
while nb_iterations is None or iteration < nb_iterations:
    print(f"\n🔄 Début de l'itération {iteration + 1}")

    # Ouvrir le navigateur
    driver = webdriver.Chrome()

    try:
        # Accéder à la page principale
        url = "https://www.btl.gov.il/Pages/default.aspx"
        driver.get(url)
        time.sleep(3)  # Attente pour chargement

        # Cliquer sur le lien "שירות אישי"
        bouton = driver.find_element(By.ID, "ctl00_Topmneu_HyperLink9")
        bouton.click()
        print("✅ Clique sur 'שירות אישי' réussi !")
        time.sleep(3)  # Attente pour chargement

        # Saisir le numéro d'identité
        input_field = driver.find_element(By.ID, "vm_OptZehut")
        input_field.clear()
        input_field.send_keys("039020201")#
        print("✅ Numéro saisi avec succès !")
        time.sleep(2)

        # Cocher l'option "שיחה קולית"
        checkbox_label = driver.find_element(By.XPATH, "//label[@for='vm_CellMsgType$2']")
        checkbox_label.click()
        print("✅ Option 'שיחה קולית' cochée avec succès !")
        time.sleep(2)

        # Cliquer sur le bouton "שלחו לי קוד חד פעמי"
        submit_button = driver.find_element(By.NAME, "btnOpt")
        submit_button.click()
        print("✅ Bouton 'שלחו לי קוד חד פעמי' cliqué avec succès !")
        time.sleep(5)  # Attente pour voir le résultat

    except Exception as e:
        print(f"⚠️ Erreur lors de l'exécution : {e}")

    finally:
        driver.quit()
        print("🚪 Navigateur fermé.")

    # Attente avant la prochaine itération
    iteration += 1
    if nb_iterations is None or iteration < nb_iterations:
        print("⏳ Attente de 10 secondes avant la prochaine tentative...\n")
        time.sleep(10)

print("\n✅ Script terminé !")
