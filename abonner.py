import requests

TELEGRAM_BOT_TOKEN = ""

def get_chat_id():
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    response = requests.get(url)
    data = response.json()

    print(data)  # Affiche toutes les mises à jour pour voir les messages

get_chat_id()
