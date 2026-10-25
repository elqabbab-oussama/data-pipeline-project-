import urllib.request
import json
import os

url = "https://dummyjson.com/products?limit=100"
print(f"Extraction des données depuis {url}...")

# Création d'une requête avec un User-Agent pour simuler un navigateur web
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

# 1. Extraction (E de ETL)
response = urllib.request.urlopen(req)
data = json.loads(response.read())

# 2. Définition du chemin de sauvegarde vers ton dossier 'data'
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "..", "data", "raw_products.json")

# 3. Sauvegarde (Load temporaire)
with open(file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print(f"Succès ! {len(data['products'])} produits ont été sauvegardés.")