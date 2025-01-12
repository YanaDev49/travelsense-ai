import pandas as pd

def load_data():
    """Load user and train schedule data from CSV files."""
    try:
        df_users = pd.read_csv("travel_preferences.csv")
        df_trains = pd.read_csv("train_schedule.csv")
        print("Data loaded successfully.")
        return df_users, df_trains
    except FileNotFoundError as e:
        print(f"Error loading data: {e}")
        exit(1)

def generate_recommendations(df_users, df_trains):
    """Generate train recommendations based on user preferences."""
    # The generate_recommendations function joins user data from both the train schedule and travel preferences csv files to use both data when coming up with the recommended travel options
    df_users["key"] = 1
    df_trains["key"] = 1

    # where the cross join actually happens with the data (the data from the csv files being merged)
    df_merged = pd.merge(df_users, df_trains, on="key").drop(columns=["key"])

    
    print("Merged DataFrame Columns:", df_merged.columns)

    
    def match_city(user_city, train_station):
        """Return True if user city is part of the train station name."""
        return user_city.lower() in train_station.lower()

    df_merged = df_merged[
        df_merged.apply(lambda row: match_city(row["origin_x"], row["origin_y"]) and
                                    match_city(row["destination_x"], row["destination_y"]), axis=1)
    ]

    
    print("Filtered DataFrame Columns:", df_merged.columns)
    print("First few rows of filtered DataFrame:", df_merged.head())

    # This is where the recommendation logic is actually applied. 
    recommendations = []
    grouped = df_merged.groupby(["user_id", "origin_x", "destination_x"])

    for (user_id, origin, destination), group in grouped:
        row = group.iloc[0]
        is_student = row["student_discount"]
        wants_first_class = row["first_class"]

        # For example if the user is a student it will reccomend student dicount or cheapest travel fair. if the user wants first class the system will make sure that it reccomends first class
        if is_student:
            best_option = group.loc[group["average_price"].idxmin()]
            reason = "Cheapest overall (Student Discount)"
        elif wants_first_class:
            fc_rows = group[group["train_class"] == "First Class"]
            if not fc_rows.empty:
                best_option = fc_rows.loc[fc_rows["average_price"].idxmin()]
                reason = "Cheapest First Class"
            else:
                best_option = group.loc[group["average_price"].idxmin()]
                reason = "Fallback to Cheapest"
        else:
            median_price = group["average_price"].median()
            closest_idx = (group["average_price"] - median_price).abs().idxmin()
            best_option = group.loc[closest_idx]
            reason = "Closest to Median Price"

        recommendations.append({
            "user_id": user_id,  
            "origin": origin,
            "destination": destination,
            "chosen_train_origin": best_option["origin_y"],
            "chosen_train_destination": best_option["destination_y"],
            "departure_date": best_option["departure_date"],
            "departure_time": best_option["departure_time"],
            "train_class": best_option["train_class"],
            "price": best_option["average_price"],
            "recommendation_reason": reason
        })

    df_recs = pd.DataFrame(recommendations)
    print("Generated Recommendations DataFrame:", df_recs.head())  
    return df_recs


def get_user_recommendation(user_id, df_recs):
    """Fetch recommendation for a specific user."""
    
    print("Columns in df_recs:", df_recs.columns)

    if "user_id" not in df_recs.columns:
        raise KeyError("The column 'user_id' is missing in df_recs. Check your DataFrame construction in generate_recommendations.")
    
    user_rec = df_recs[df_recs["user_id"] == user_id]
    if not user_rec.empty:
        return user_rec.iloc[0].to_dict()
    return None
