# EDOH AFI / MS IA SEM 2

import pandas as pd
import matplotlib.pyplot as plt

#  Récupération du jeu de donnee
data_url = "C:/Users/Afia Faith/Downloads/ExamAfi/data/raw/raw_data.csv"
data = pd.read_csv(data_url)

# Nettoyer les données: suppression des lignes avec des valeurs manquantes
data = data.dropna()

# Notre anlyse ne concernera que le nombre de films realises par un auteur dans une ville donnee donc nous allons selectionner que 4 tables de notre donnee

data = data[['titre', 'realisateur', 'nombre_de_film', 'ville']]

# Faire du feature engineering: nous allons creer une nouvelle colonne qui titre_realisateur
data['titre_realisateur'] = data['titre'] * data['realisateur']

# Statistiques sommaires de notre donnee
summary_stats = data.describe()
print(summary_stats)

# Sauvegarde des données nettoyées et transformées dans le dossier cleaned
data.to_csv('cleaned.csv', index=False)

