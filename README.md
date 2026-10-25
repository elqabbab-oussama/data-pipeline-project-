# data-pipeline-project-
Description du Projet
Ce projet implémente un pipeline ETL (Extract, Transform, Load) automatisé en Python. Il démontre la capacité à extraire des données e-commerce depuis une API, à les nettoyer, et à les structurer dans une base de données relationnelle.

Architecture du Pipeline

Extract (src/extract.py) : Requête HTTP avec configuration d'un User-Agent personnalisé pour contourner les blocages serveur et récupérer 100 produits bruts au format JSON.

Transform (src/transform.py) : Parsage des données brutes, filtrage des variables clés (ID, nom, catégorie, prix) et conversion en fichier CSV standardisé.

Load (src/load.py & src/query.py) : Création du schéma de table SQL, injection des données dans une base SQLite native, et exécution de requêtes analytiques (Top 5 des produits).

Environnement et Exécution

Développé sous environnement Linux (WSL Ubuntu) via Visual Studio Code.

Nécessite Python 3.x (aucune bibliothèque externe requise).

Pour exécuter le pipeline, lancez séquentiellement depuis le terminal : python3 src/extract.py, python3 src/transform.py, puis python3 src/load.py.
