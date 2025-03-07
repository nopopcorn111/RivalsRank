from flask import Flask, request
import requests

app = Flask(__name__)

# Tracker.gg API key (your provided key)
TRACKER_API_KEY = 'ceeebbaf-2e59-43a1-b659-0b1ee00da6aa'

# Marvel Rivals API URL (adjust based on Tracker.gg documentation)
TRACKER_API_URL = 'https://api.tracker.gg/api/v2/marvel-rivals/standard/profile'

@app.route('/marvelrivals', methods=['GET'])
def marvel_rivals_rank():
    user_id = request.args.get('uid')  # Get the user ID from the query string
    
    # Make the request to Tracker.gg API
    response = requests.get(
        f'{TRACKER_API_URL}/{user_id}',
        headers={'TRN-Api-Key': TRACKER_API_KEY}
    )
    
    if response.status_code == 200:
        data = response.json()
        try:
            rank = data['data']['segments'][0]['stats']['rank']['displayValue']
            return rank  # Only return the rank, no UID
        except KeyError:
            return 'Error: Could not retrieve rank.'
    else:
        return 'Error: Unable to fetch data for the specified user.'

# Ensure the app runs properly on Koyeb
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)  # Use port 8000
