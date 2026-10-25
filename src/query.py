import sqlite3
import os

# Connexion à la base de données
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "..", "data", "ecommerce.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Requête SQL : on demande les 5 produits les plus chers
cursor.execute("SELECT title, category, price FROM products ORDER BY price DESC LIMIT 5")
results = cursor.fetchall()

print("\n--- TOP 5 DES PRODUITS LES PLUS CHERS ---")
for row in results:
    print(f"- {row[0]} ({row[1]}) : {row[2]} $")

conn.close()