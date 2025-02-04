import requests

TELEGRAM_BOT_TOKEN = "8076057702:AAHZIWauDxm5NP9Aq9ryHM-tyzCfmLZqja0"

def get_chat_id():
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    response = requests.get(url)
    data = response.json()

    print(data)  # Affiche toutes les mises à jour pour voir les messages

get_chat_id()
