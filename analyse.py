import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Créer le dossier data s'il n'existe pas
os.makedirs('data', exist_ok=True)

# Récupération du prix du Bitcoin
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
data = requests.get(url).json()
prix = data["bitcoin"]["usd"]

# Enregistrer dans un CSV
df = pd.DataFrame([[datetime.now(), prix]], columns=["date", "prix"])
df.to_csv("data/prix_bitcoin.csv", mode='a', header=False, index=False)

# Calcul de la moyenne mobile sur les 5 derniers points
data = pd.read_csv("data/prix_bitcoin.csv", names=["date", "prix"])
data["moyenne_mobile"] = data["prix"].rolling(5).mean()

# Graphique
plt.figure(figsize=(8,4))
plt.plot(data["prix"], label="Prix BTC/USD")
plt.plot(data["moyenne_mobile"], label="Moyenne mobile (5 points)")
plt.legend()
plt.title("Analyse technique du Bitcoin")
plt.savefig("data/graphique.png")

print("Analyse terminée et graphique mis à jour.")