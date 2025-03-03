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
            return f'{user_id}\'s Marvel Rivals Rank: {rank}'
        except KeyError:
            return f'Error: Could not retrieve rank for {user_id}.'
    else:
        return f'Error: Unable to fetch data for {user_id}.'

if __name__ == '__main__':
    app.run(debug=True)
