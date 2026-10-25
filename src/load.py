import csv
import sqlite3
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, "..", "data", "cleaned_products.csv")
db_path = os.path.join(current_dir, "..", "data", "ecommerce.db")

print("Connexion à la base de données SQLite...")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Création de la table SQL
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    title TEXT,
    category TEXT,
    price REAL
)
''')
cursor.execute('DELETE FROM products') # Évite les doublons en cas de relance

# Lecture du CSV et insertion
with open(input_path, "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    data = [(row['id'], row['title'], row['category'], row['price']) for row in reader]
    
    cursor.executemany('INSERT INTO products (id, title, category, price) VALUES (?, ?, ?, ?)', data)

conn.commit()
conn.close()

print(f"Succès ! {len(data)} produits ont été chargés dans ecommerce.db.")