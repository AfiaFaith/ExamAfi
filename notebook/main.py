# EDOH AFI / MS IA SEM 2

import os
import pandas as pd

# Récupération du jeu de données depuis un chemin local
data_path = "../data/raw/raw_data.csv"
data = pd.read_csv(data_path)

# Nettoyer les données : suppression des lignes avec des valeurs manquantes
data = data.dropna()

# Notre analyse ne concernera que le nombre de films réalisés par un auteur dans une ville donnée, donc nous allons sélectionner que 4 colonnes de notre donnée
data = data[['titre', 'realisateur', 'nombre_de_film', 'Ville']]

# Faire du feature engineering : nous allons créer une nouvelle colonne "titre_realisateur"
data['titre_realisateur'] = data['titre'] + '_' + data['realisateur']  # Utilisation de '+' pour concaténer les valeurs

# Statistiques sommaires de notre donnée
summary_stats = data.describe()
print(summary_stats)

# Création du répertoire "cleaned" s'il n'existe pas
output_directory = 'data/cleaned'
os.makedirs(output_directory, exist_ok=True)

# Sauvegarde des données nettoyées dans le dossier "data/cleaned"
data.to_csv(os.path.join(output_directory, 'cleaned.csv'), index=False)