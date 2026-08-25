import pandas as pd
import os

folder_path = r"C:\Users\Amisha Shetty\Downloads\Food Project"

print("Files in folder:")
print(os.listdir(folder_path))

# ✅ Read CSV (correct)
providers = pd.read_csv(os.path.join(folder_path, "providers_data.csv"))
receivers = pd.read_csv(os.path.join(folder_path, "receivers_data.csv"))
food = pd.read_csv(os.path.join(folder_path, "food_listings_data.csv"))
claims = pd.read_csv(os.path.join(folder_path, "claims_data.csv"))

# Clean column names
providers.columns = providers.columns.str.strip()
receivers.columns = receivers.columns.str.strip()
food.columns = food.columns.str.strip()
claims.columns = claims.columns.str.strip()

# Remove duplicates
providers.drop_duplicates(inplace=True)
receivers.drop_duplicates(inplace=True)
food.drop_duplicates(inplace=True)
claims.drop_duplicates(inplace=True)

# Clean text fields
providers['City'] = providers['City'].astype(str).str.strip().str.title()
receivers['City'] = receivers['City'].astype(str).str.strip().str.title()
food['Location'] = food['Location'].astype(str).str.strip().str.title()

if 'Provider_Type' in food.columns:
    food['Provider_Type'] = food['Provider_Type'].astype(str).str.strip().str.title()

if 'Food_Type' in food.columns:
    food['Food_Type'] = food['Food_Type'].astype(str).str.strip().str.title()

if 'Meal_Type' in food.columns:
    food['Meal_Type'] = food['Meal_Type'].astype(str).str.strip().str.title()

if 'Status' in claims.columns:
    claims['Status'] = claims['Status'].astype(str).str.strip().str.title()

# Date conversion
if 'Expiry_Date' in food.columns:
    food['Expiry_Date'] = pd.to_datetime(food['Expiry_Date'], errors='coerce')

if 'Timestamp' in claims.columns:
    claims['Timestamp'] = pd.to_datetime(claims['Timestamp'], errors='coerce')

# Save cleaned files
providers.to_csv(os.path.join(folder_path, "providers_data_cleaned.csv"), index=False)
receivers.to_csv(os.path.join(folder_path, "receivers_data_cleaned.csv"), index=False)
food.to_csv(os.path.join(folder_path, "food_listings_data_cleaned.csv"), index=False)
claims.to_csv(os.path.join(folder_path, "claims_data_cleaned.csv"), index=False)

print("✅ Cleaning complete")