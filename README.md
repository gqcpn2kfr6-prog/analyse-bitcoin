# 📊 Analyse Bitcoin Automatique

Ce projet effectue une analyse technique automatique du prix du Bitcoin toutes les heures grâce aux GitHub Actions.

## 🚀 Fonctionnalités

- ✅ Récupération automatique du prix Bitcoin via l'API CoinGecko
- 📈 Calcul de la moyenne mobile sur 5 points
- 📊 Génération de graphiques d'analyse technique
- ⏰ Exécution automatique toutes les heures
- 💾 Sauvegarde des données historiques en CSV

## 📁 Structure du projet

```
analyse-bitcoin/
├── analyse.py              # Script principal d'analyse
├── requirements.txt        # Dépendances Python
├── data/                   # Dossier des résultats
│   ├── prix_bitcoin.csv    # Données historiques
│   └── graphique.png       # Graphique d'analyse
└── .github/workflows/
    └── analyse-auto.yml    # Automatisation GitHub Actions
```

## 🔧 Installation locale

1. Cloner le dépôt :
```bash
git clone https://github.com/gqcpn2kfr6-prog/analyse-bitcoin.git
cd analyse-bitcoin
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Lancer l'analyse :
```bash
python analyse.py
```

## ⚙ï¸ Automatisation

Le workflow GitHub Actions s'exécute :
- 🕰️ **Automatiquement** : toutes les heures
- 🔄 **Manuellement** : via l'onglet "Actions" du dépôt

Les résultats sont automatiquement commités dans le dossier `data/`.

## 📊 Résultats

- **prix_bitcoin.csv** : Historique complet des prix avec horodatage
- **graphique.png** : Visualisation du prix et de la moyenne mobile

---

💡 *Projet créé pour démontrer l'automatisation d'analyses financières avec GitHub Actions*