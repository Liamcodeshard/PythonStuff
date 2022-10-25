import os
travel_log = {
    "France": {"cities_visited" :["Paris","Lille","Dijon"]},
    "Germany":{"cities_visited": ["Berlin", "Whatever", ]},
    "Italy":{"cities_visited": ["Milan", "Cinque Terre", "Lago Como", "Amalfi", "Napoli"]}
}

print(travel_log["France"]["cities_visited"][0])
