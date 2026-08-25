USE food_management;
-- ####################################################
-- Local Food Wastage Management System SQL Queries
-- ####################################################

-- ##############################
-- A. Food Providers & Receivers
-- ##############################

-- 1. Number of food providers per city
SELECT City, COUNT(*) AS Num_Providers
FROM Providers
GROUP BY City;

-- 2. Number of receivers per city
SELECT City, COUNT(*) AS Num_Receivers
FROM Receivers
GROUP BY City;

-- 3. Providers with most contributions
SELECT p.Name, COUNT(f.Food_ID) AS Food_Contributed
FROM Providers p
JOIN Food_Listings f ON p.Provider_ID = f.Provider_ID
GROUP BY p.Name
ORDER BY Food_Contributed DESC
LIMIT 10;

-- 4. Contact info of providers in a specific city
SELECT Name, Contact
FROM Providers
WHERE City='New Jessica';

-- ##############################
-- B. Food Listings & Availability
-- ##############################

-- 5. Total quantity of food available
SELECT SUM(Quantity) AS Total_Food
FROM Food_Listings;

-- 6. City with the highest number of food listings
SELECT Location, COUNT(*) AS Num_Listings
FROM Food_Listings
GROUP BY Location
ORDER BY Num_Listings DESC
LIMIT 1;

-- 7. Most commonly available food types
SELECT Food_Type, COUNT(*) AS Count
FROM Food_Listings
GROUP BY Food_Type
ORDER BY Count DESC;

-- ##############################
-- C. Claims & Distribution
-- ##############################

-- 8. Number of claims per food item
SELECT Food_ID, COUNT(*) AS Num_Claims
FROM Claims
GROUP BY Food_ID;

-- 9. Provider with most completed claims
SELECT p.Name, COUNT(cl.Claim_ID) AS Completed_Claims
FROM Claims cl
JOIN Food_Listings f ON cl.Food_ID = f.Food_ID
JOIN Providers p ON f.Provider_ID = p.Provider_ID
WHERE cl.Status='Completed'
GROUP BY p.Name
ORDER BY Completed_Claims DESC
LIMIT 5;

-- 10. Percentage of claims by status
SELECT Status, COUNT(*)*100.0/(SELECT COUNT(*) FROM Claims) AS Percentage
FROM Claims
GROUP BY Status;

-- ##############################
-- D. Analysis & Insights
-- ##############################

-- 11. Average quantity claimed per receiver
SELECT cl.Receiver_ID, AVG(f.Quantity) AS Avg_Quantity
FROM Claims cl
JOIN Food_Listings f ON cl.Food_ID = f.Food_ID
GROUP BY cl.Receiver_ID;

-- 12. Most claimed meal type
SELECT f.Meal_Type, COUNT(*) AS Count
FROM Claims cl
JOIN Food_Listings f ON cl.Food_ID = f.Food_ID
GROUP BY f.Meal_Type
ORDER BY Count DESC;

-- 13. Total quantity donated per provider
SELECT p.Name, SUM(f.Quantity) AS Total_Quantity
FROM Food_Listings f
JOIN Providers p ON f.Provider_ID = p.Provider_ID
GROUP BY p.Name
ORDER BY Total_Quantity DESC;

-- 14. Top 5 receivers with most claims
SELECT r.Name, COUNT(cl.Claim_ID) AS Num_Claims
FROM Receivers r
JOIN Claims cl ON r.Receiver_ID = cl.Receiver_ID
GROUP BY r.Name
ORDER BY Num_Claims DESC
LIMIT 5;

-- 15. Food types with highest claims
SELECT f.Food_Type, COUNT(cl.Claim_ID) AS Num_Claims
FROM Food_Listings f
JOIN Claims cl ON f.Food_ID = cl.Food_ID
GROUP BY f.Food_Type
ORDER BY Num_Claims DESC;