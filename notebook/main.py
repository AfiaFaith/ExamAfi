# EDOH AFI / MS IA SEM 2

import os
import pandas as pd

# Constantes pour les chemins d'accès aux fichiers
DATA_PATH = "../data/raw/raw_data.csv"
OUTPUT_DIRECTORY = 'data/cleaned'

try:
    # Récupération du jeu de données depuis un chemin local
    data = pd.read_csv(DATA_PATH)

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
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

    # Sauvegarde des données nettoyées dans le dossier "data/cleaned"
    data.to_csv(os.path.join(OUTPUT_DIRECTORY, 'cleaned.csv'), index=False)

except FileNotFoundError as e:
    print(f"Erreur: Le fichier de données '{DATA_PATH}' n'a pas été trouvé. Veuillez vérifier le chemin d'accès.")
    # Gérer l'erreur ici ou ajouter une sortie propre
except Exception as e:
    print(f"Une erreur inattendue s'est produite: {str(e)}")
    # Gérer l'erreur ici ou ajouter une sortie propre
