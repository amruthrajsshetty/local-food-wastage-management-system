import sqlite3
import pandas as pd

conn = sqlite3.connect("food_wastage.db")

queries = {
    "1. Providers count by city": """
        SELECT City, COUNT(*) AS total_providers
        FROM providers
        GROUP BY City
        ORDER BY total_providers DESC
    """,

    "2. Receivers count by city": """
        SELECT City, COUNT(*) AS total_receivers
        FROM receivers
        GROUP BY City
        ORDER BY total_receivers DESC
    """,

    "3. Provider type contributing most food": """
        SELECT Provider_Type, SUM(Quantity) AS total_quantity
        FROM food_listings
        GROUP BY Provider_Type
        ORDER BY total_quantity DESC
    """,

    "4. Contact information of providers": """
        SELECT Name, Contact, City
        FROM providers
        ORDER BY City
    """,

    "5. Receivers who claimed the most food": """
        SELECT r.Name, COUNT(c.Claim_ID) AS total_claims
        FROM claims c
        JOIN receivers r ON c.Receiver_ID = r.Receiver_ID
        GROUP BY r.Name
        ORDER BY total_claims DESC
    """,

    "6. Total quantity of food available": """
        SELECT SUM(Quantity) AS total_food_available
        FROM food_listings
    """,

    "7. City with highest number of food listings": """
        SELECT Location, COUNT(*) AS total_listings
        FROM food_listings
        GROUP BY Location
        ORDER BY total_listings DESC
    """,

    "8. Most commonly available food types": """
        SELECT Food_Type, COUNT(*) AS total_items
        FROM food_listings
        GROUP BY Food_Type
        ORDER BY total_items DESC
    """,

    "9. Food claims for each food item": """
        SELECT f.Food_Name, COUNT(c.Claim_ID) AS total_claims
        FROM claims c
        JOIN food_listings f ON c.Food_ID = f.Food_ID
        GROUP BY f.Food_Name
        ORDER BY total_claims DESC
    """,

    "10. Provider with highest successful food claims": """
        SELECT p.Name, COUNT(c.Claim_ID) AS successful_claims
        FROM claims c
        JOIN food_listings f ON c.Food_ID = f.Food_ID
        JOIN providers p ON f.Provider_ID = p.Provider_ID
        WHERE c.Status = 'Completed'
        GROUP BY p.Name
        ORDER BY successful_claims DESC
    """,

    "11. Percentage of completed vs pending vs cancelled claims": """
        SELECT Status,
               ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM claims), 2) AS percentage
        FROM claims
        GROUP BY Status
    """,

    "12. Average quantity claimed per receiver": """
        SELECT r.Name, ROUND(AVG(f.Quantity), 2) AS avg_quantity
        FROM claims c
        JOIN receivers r ON c.Receiver_ID = r.Receiver_ID
        JOIN food_listings f ON c.Food_ID = f.Food_ID
        GROUP BY r.Name
        ORDER BY avg_quantity DESC
    """,

    "13. Meal type claimed the most": """
        SELECT f.Meal_Type, COUNT(c.Claim_ID) AS total_claims
        FROM claims c
        JOIN food_listings f ON c.Food_ID = f.Food_ID
        GROUP BY f.Meal_Type
        ORDER BY total_claims DESC
    """,

    "14. Total quantity donated by each provider": """
        SELECT p.Name, SUM(f.Quantity) AS total_donated
        FROM food_listings f
        JOIN providers p ON f.Provider_ID = p.Provider_ID
        GROUP BY p.Name
        ORDER BY total_donated DESC
    """,

    "15. Food items expiring soon": """
        SELECT Food_Name, Quantity, Expiry_Date, Location
        FROM food_listings
        ORDER BY Expiry_Date ASC
    """
}

for title, query in queries.items():
    print("\n" + "="*60)
    print(title)
    print("="*60)
    df = pd.read_sql_query(query, conn)
    print(df)

conn.close()