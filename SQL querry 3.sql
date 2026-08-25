-- Food_Listings references Providers
SELECT * 
FROM Food_Listings f
LEFT JOIN Providers p ON f.Provider_ID = p.Provider_ID
WHERE p.Provider_ID IS NULL;

-- Claims references Food_Listings
SELECT * 
FROM Claims cl
LEFT JOIN Food_Listings f ON cl.Food_ID = f.Food_ID
WHERE f.Food_ID IS NULL;

-- Claims references Receivers
SELECT * 
FROM Claims cl
LEFT JOIN Receivers r ON cl.Receiver_ID = r.Receiver_ID
WHERE r.Receiver_ID IS NULL; 
SELECT COUNT(*) AS ProvidersCount FROM Providers;
SELECT COUNT(*) AS ReceiversCount FROM Receivers;
SELECT COUNT(*) AS FoodListingsCount FROM Food_Listings;
SELECT COUNT(*) AS ClaimsCount FROM Claims;