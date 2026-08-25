import sqlite3
import pandas as pd
import os

folder_path = r"C:\Users\Amisha Shetty\Downloads\Food Project"
conn = sqlite3.connect(os.path.join(folder_path, "food_wastage.db"))

print("\nProviders Table:")
print(pd.read_sql("SELECT * FROM providers LIMIT 5", conn))

print("\nReceivers Table:")
print(pd.read_sql("SELECT * FROM receivers LIMIT 5", conn))

print("\nFood Listings Table:")
print(pd.read_sql("SELECT * FROM food_listings LIMIT 5", conn))

print("\nClaims Table:")
print(pd.read_sql("SELECT * FROM claims LIMIT 5", conn))

conn.close()