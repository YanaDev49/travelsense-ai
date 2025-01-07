from flask import Flask, request, render_template, jsonify, redirect, url_for
import model
import redis
import os

app = Flask(__name__, static_folder='static')

# Connect to Redis using environment variables for the host and port.
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

# Load the data and prepare initial recommendations as soon as the app starts.
df_users, df_trains = model.load_data()
df_recs = model.generate_recommendations(df_users, df_trains)

# This function generates a personalised itinerary for a given user.
def generate_itinerary(user_id):
    user_rec = model.get_user_recommendation(user_id, df_recs)
    if not user_rec:
        return None
    return {
        "greeting": f"Happy Travels {user_id}! Here’s your personalised itinerary:",
        "places": [
            "Duomo di Milano - An iconic cathedral in Milan.", 
            "Galleria Vittorio Emanuele II - A historic shopping arcade"
        ],
        "restaurants": [
            "Vegan options: Joia - Fine dining for vegans.", 
            "Gluten-free: GluFree Bakery - Delicious and safe dining.", 
            "Pescatarian: Langosteria - Exceptional seafood."
        ],
        "train_stations": [
            "Milano Centrale - The main hub to explore Italy.", 
            "Cadorna Station - For access to local landmarks."
        ],
        "tips": [
            "Buy tickets in advance to save money.", 
            "Use public transport to explore the city efficiently."
        ],
        "predicted_cheapest_fare": user_rec["price"],
        "recommendation_reason": user_rec["recommendation_reason"],
        "chosen_train": {
            "origin": user_rec["chosen_train_origin"],
            "destination": user_rec["chosen_train_destination"],
            "departure_date": user_rec["departure_date"],
            "departure_time": user_rec["departure_time"],
            "train_class": user_rec["train_class"],
            "price": user_rec["price"]
        }
    }

# Displays the homepage.
@app.route('/')
def home():
    return render_template('index.html')

# Tests the Redis connection by saving and retrieving a test key.
@app.route('/test-redis')
def test_redis_connection():
    try:
        redis_client.set("test_key", "3")
        test_value = redis_client.get("test_key")
        return jsonify({"message": "Redis connected successfully!", "test_value": test_value}), 200
    except Exception as e:
        return jsonify({"error": f"Redis connection failed: {e}"}), 500

# Handles both GET and POST requests for recommendations and questionnaire submissions.
@app.route('/recommend', methods=['GET', 'POST'])
def recommend_and_handle_questionnaire():
    if request.method == 'POST':
        user_id = "Trainliner"
        # Check if the incoming request contains JSON data.
        if request.content_type == 'application/json':
            # Parse the JSON payload from the request.
            data = request.get_json()
            print(f"Received JSON data: {data}")

            if not data:
                print("No JSON data received or invalid format.")
            else:
                # Save the JSON data to Redis under the user ID.
                redis_client.hset(f"user:{user_id}:questionnaire", mapping=data)
                print(f"Data saved to Redis for user {user_id}: {data}")
        else:
            # Ignore any requests that aren't JSON.
            print(f"Ignoring request with unsupported Content-Type: {request.content_type}")

        # Generate an itinerary using the saved data.
        itinerary = generate_itinerary(user_id)
        if not itinerary:
            return jsonify({"error": "Could not generate itinerary."}), 500

        # Render and return the itinerary page.
        print("Redirecting to itinerary...")
        return render_template('itinerary.html', itinerary=itinerary)

    else:
        # Handle GET requests by generating an itinerary for a default user.
        user_id = "Trainliner"
        itinerary = generate_itinerary(user_id)

        if not itinerary:
            return "User not found!", 404

        # Render and return the results page.
        return render_template('results.html', itinerary=itinerary)

# Runs the Flask application on port 5000.
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
