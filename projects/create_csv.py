import pandas as pd

# -------------------------
# 1) Define User Data
# -------------------------
USER_DATA = {
    "Trainliner": {
        "name": "Jane Doe",
        "travel_history": [
            {"origin": "London", "destination": "Manchester", "date": "2024-12-01"},
            {"origin": "London", "destination": "Milan", "date": "2024-12-05"}
        ],
        "preferences": {
            "cheapest_fare": True,
            "student_discount": True,
            "fastest_route": True,
            "refundable_tickets": True,
            "sleeper_trains": True,
            "first_class": True,
            "short_trips_preferred": True,
            "step_free_access": False,
            "priority_boarding": False,
            "updates_delays_cancellations": True,
        }
    }
}

# -------------------------
# 2) Create travel_preferences.csv
# -------------------------
user_data_rows = []
for user_id, user_info in USER_DATA.items():
    for trip in user_info["travel_history"]:
        travel_preferences = user_info["preferences"]
        row = {
            "user_id": user_id,
            "origin": trip["origin"],
            "destination": trip["destination"],
            "date": trip["date"],
            **travel_preferences
        }
        user_data_rows.append(row)

df_users = pd.DataFrame(user_data_rows)
df_users.to_csv("travel_preferences.csv", index=False)
print("travel_preferences.csv created successfully!")

# -------------------------
# 3) Define Train Schedule Data
# -------------------------
# Mock train schedule data from London to Milan
train_schedule_data = [
    {"origin": "London Euston", "destination": "Milan Centrale", "departure_date": "2024-12-01", "departure_time": "08:00", "train_class": "Standard", "average_price": 120},
    {"origin": "London Euston", "destination": "Milan Centrale", "departure_date": "2024-12-01", "departure_time": "08:00", "train_class": "First Class", "average_price": 180},
    {"origin": "London St Pancras", "destination": "Milan Centrale", "departure_date": "2024-12-02", "departure_time": "09:30", "train_class": "Standard", "average_price": 150},
    {"origin": "London St Pancras", "destination": "Milan Centrale", "departure_date": "2024-12-02", "departure_time": "09:30", "train_class": "First Class", "average_price": 220},
    {"origin": "London Euston", "destination": "Milan Centrale", "departure_date": "2024-12-03", "departure_time": "10:00", "train_class": "Standard", "average_price": 130},
    {"origin": "London Euston", "destination": "Milan Centrale", "departure_date": "2024-12-03", "departure_time": "10:00", "train_class": "First Class", "average_price": 200},
    {"origin": "London Euston", "destination": "Milan Centrale", "departure_date": "2024-12-04", "departure_time": "14:00", "train_class": "Standard", "average_price": 125},
    {"origin": "London Euston", "destination": "Milan Centrale", "departure_date": "2024-12-04", "departure_time": "14:00", "train_class": "First Class", "average_price": 195},
    {"origin": "London St Pancras", "destination": "Milan Centrale", "departure_date": "2024-12-05", "departure_time": "11:30", "train_class": "Standard", "average_price": 140},
    {"origin": "London St Pancras", "destination": "Milan Centrale", "departure_date": "2024-12-05", "departure_time": "11:30", "train_class": "First Class", "average_price": 210},
]



df_trains = pd.DataFrame(train_schedule_data)
df_trains.to_csv("train_schedule.csv", index=False)
print("train_schedule.csv created successfully!")
