import pandas as pd
import sqlite3
import os

folder_path = r"C:\Users\Amisha Shetty\Downloads\Food Project"

# Connect to database
conn = sqlite3.connect(os.path.join(folder_path, "food_wastage.db"))

# Read cleaned CSV files
providers = pd.read_csv(os.path.join(folder_path, "providers_data_cleaned.csv"))
receivers = pd.read_csv(os.path.join(folder_path, "receivers_data_cleaned.csv"))
food = pd.read_csv(os.path.join(folder_path, "food_listings_data_cleaned.csv"))
claims = pd.read_csv(os.path.join(folder_path, "claims_data_cleaned.csv"))

# Insert into SQL tables
providers.to_sql("providers", conn, if_exists="replace", index=False)
receivers.to_sql("receivers", conn, if_exists="replace", index=False)
food.to_sql("food_listings", conn, if_exists="replace", index=False)
claims.to_sql("claims", conn, if_exists="replace", index=False)

conn.close()

print("Cleaned data inserted into database successfully")