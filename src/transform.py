import json
import csv
import os

# 1. Définition des chemins vers ton dossier 'data'
current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, "..", "data", "raw_products.json")
output_path = os.path.join(current_dir, "..", "data", "cleaned_products.csv")

print("Lecture des données brutes...")

# 2. Lecture du fichier JSON téléchargé à l'étape précédente
with open(input_path, "r", encoding="utf-8") as file:
    raw_data = json.load(file)

products = raw_data.get("products", [])
cleaned_data = []

# 3. Transformation : on filtre pour ne garder que 4 colonnes
for item in products:
    cleaned_item = {
        "id": item.get("id"),
        "title": item.get("title"),
        "category": item.get("category"),
        "price": item.get("price")
    }
    cleaned_data.append(cleaned_item)

print(f"Nettoyage terminé. Sauvegarde de {len(cleaned_data)} produits...")

# 4. Sauvegarde dans un nouveau fichier CSV
with open(output_path, "w", encoding="utf-8", newline='') as csvfile:
    fieldnames = ["id", "title", "category", "price"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(cleaned_data)

print("Succès ! Le fichier cleaned_products.csv a été généré.")