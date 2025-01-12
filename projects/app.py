from flask import Flask, request, render_template, jsonify, redirect, url_for
import model
import redis
import os

app = Flask(__name__, static_folder='static')


redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)


df_users, df_trains = model.load_data()
df_recs = model.generate_recommendations(df_users, df_trains)

# This is the function that generates a personalised itinerary for our trainliner ruby specifically:) it takes the user ID and retrieves the users preloaded data and structures the itinerary
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


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/test-redis')
def test_redis_connection():
    try:
        redis_client.set("test_key", "3")
        test_value = redis_client.get("test_key")
        return jsonify({"message": "Redis connected successfully!", "test_value": test_value}), 200
    except Exception as e:
        return jsonify({"error": f"Redis connection failed: {e}"}), 500

# The /recommend route handles both GET and POST requests for saving user data in redis and displaying the generated itinerary.
@app.route('/recommend', methods=['GET', 'POST'])
def recommend_and_handle_questionnaire():
    if request.method == 'POST':
        user_id = "Trainliner"
        
        if request.content_type == 'application/json':
            
            data = request.get_json()
            print(f"Received JSON data: {data}")

            if not data:
                print("No JSON data received or invalid format.")
            else:
                
                redis_client.hset(f"user:{user_id}:questionnaire", mapping=data)
                print(f"Data saved to Redis for user {user_id}: {data}")
        else:
            
            print(f"Ignoring request with unsupported Content-Type: {request.content_type}")

        
        itinerary = generate_itinerary(user_id)
        if not itinerary:
            return jsonify({"error": "Could not generate itinerary."}), 500

        
        print("Redirecting to itinerary...")
        return render_template('itinerary.html', itinerary=itinerary)

    else:
        
        user_id = "Trainliner"
        itinerary = generate_itinerary(user_id)

        if not itinerary:
            return "User not found!", 404

        
        return render_template('results.html', itinerary=itinerary)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
