import requests
from flask import Blueprint, render_template, jsonify, request

class MainRoutes:
    def __init__(self):
        # Create a Blueprint for the main routes
        self.blueprint = Blueprint('main', __name__)
        self.register_routes()

    def register_routes(self):
        # Define route handlers
        @self.blueprint.route('/')
        def index():
            return render_template('index.html')

        @self.blueprint.route('/neos')
        def neos():
            return render_template('neos.html')

        @self.blueprint.route('/api/neos_sorted')
        def neos_sorted():
            page = request.args.get('page', 1, type=int)  # Get page number from query parameter
            nasa_api_url = 'https://api.nasa.gov/neo/rest/v1/neo/browse'
            params = {
                'api_key': 'rLRKUXWfw4ovsAi6uHCvT9wEsJxrIZz9sSTSsuxU',  # Replace with your NASA API key
                'page': page,
                'size': 20  # Limit the size to 20 NEOs per request for efficiency
            }

            response = requests.get(nasa_api_url, params=params)

            if response.status_code != 200:
                return jsonify({'error': 'Failed to fetch data from NASA API'}), 500

            data = response.json()

            # Extract relevant NEO data
            neos_data = [
                {
                    'name': neo['name'],
                    'id': neo['id'],
                    'estimated_diameter': neo['estimated_diameter']['meters']['estimated_diameter_max'],
                    'close_approach_data': neo['close_approach_data'][0] if neo['close_approach_data'] else {}
                }
                for neo in data['near_earth_objects']
                if neo['close_approach_data']
            ]

            # Sort NEOs by distance from Earth in ascending order
            neos_data.sort(key=lambda x: float(x['close_approach_data']['miss_distance']['kilometers']))
            return jsonify({'neos': neos_data, 'total_pages': data['page']['total_pages']})
