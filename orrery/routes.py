import requests
from flask import Blueprint, render_template, jsonify, request

class MainRoutes:
    def __init__(self):
        self.blueprint = Blueprint('main', __name__)
        self.register_routes()

    def register_routes(self):
        @self.blueprint.route('/')
        def index():
            return render_template('index.html')

        @self.blueprint.route('/neos')
        def neos():
            return render_template('neos.html')

        @self.blueprint.route('/api/neos_list')
        def neos_list():
            # Fetch a list of valid NEOs using the NASA NEO browse API
            page = request.args.get('page', 1, type=int)
            nasa_api_url = 'https://api.nasa.gov/neo/rest/v1/neo/browse'
            params = {
                'api_key': 'gQRlC3BcoHQYhGoIijg8TqUGUt9nQ2U9wL696FTP',  # Replace with your actual NASA API key
                'page': page,
                'size': 10  # Limit the number of NEOs per page for efficiency
            }

            try:
                response = requests.get(nasa_api_url, params=params)
                response.raise_for_status()  # Raise error for HTTP status codes 4xx/5xx
                data = response.json()

                neos_data = [
                    {
                        'id': neo['id'],
                        'name': neo['name'],
                        'estimated_diameter': neo['estimated_diameter']['meters']['estimated_diameter_max'],
                        'close_approach_date': neo['close_approach_data'][0]['close_approach_date'] if neo['close_approach_data'] else "Unknown",
                    }
                    for neo in data['near_earth_objects']
                ]

                return jsonify({'neos': neos_data, 'total_pages': data['page']['total_pages'], 'total_neos': data['page']['total_elements']})

            except requests.exceptions.RequestException as e:
                print(f"Error fetching NEO list: {e}")
                return jsonify({'error': 'Failed to fetch NEO list', 'details': str(e)}), 500

        @self.blueprint.route('/api/neo_details')
        def neo_details():
            neo_id = request.args.get('neo_id')
            if not neo_id:
                return jsonify({'error': 'No NEO ID provided'}), 400

            try:
                # Get NEO details from the NASA API
                nasa_api_url = f'https://api.nasa.gov/neo/rest/v1/neo/{neo_id}'
                params = {'api_key': 'gQRlC3BcoHQYhGoIijg8TqUGUt9nQ2U9wL696FTP'}  # Replace with your actual NASA API key
                response = requests.get(nasa_api_url, params=params)
                response.raise_for_status()
                neo_data = response.json()

                # Get additional details from the JPL Small Body Database
                jpl_data = self.fetch_jpl_data(neo_id)

                # Generate a description and fun fact
                description = self.generate_description(neo_data)
                fun_fact = self.generate_fun_fact(neo_data)

                # Combine data from both sources
                combined_data = {
                    'name': neo_data.get('name', 'Unknown'),
                    'id': neo_id,
                    'estimated_diameter': neo_data.get('estimated_diameter', {}).get('meters', {}).get('estimated_diameter_max', 'Unknown'),
                    'close_approach_data': neo_data['close_approach_data'][0] if neo_data.get('close_approach_data') else {},
                    'absolute_magnitude': neo_data.get('absolute_magnitude_h', 'Unknown'),
                    'orbital_data': jpl_data.get('orbital_data', {}) if jpl_data else {},
                    'description': description,
                    'fun_fact': fun_fact
                }

                return jsonify({'neo': combined_data})

            except requests.exceptions.RequestException as e:
                return jsonify({'error': 'Failed to fetch data', 'details': str(e)}), 500

    def fetch_jpl_data(self, neo_id):
        jpl_api_url = f'https://ssd-api.jpl.nasa.gov/sbdb.api?sstr={neo_id}&full-prec=true'
        try:
            response = requests.get(jpl_api_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching JPL data for NEO ID {neo_id}: {e}")
            return {}


    def generate_description(self, neo_data):
        name = neo_data.get('name', 'Unknown')
        diameter = neo_data.get('estimated_diameter', {}).get('meters', {}).get('estimated_diameter_max', 'Unknown')
        magnitude = neo_data.get('absolute_magnitude_h', 'Unknown')
        return f"{name} is a Near-Earth Object with an estimated diameter of {diameter} meters and an absolute magnitude of {magnitude}."

    def generate_fun_fact(self, neo_data):
        diameter = neo_data.get('estimated_diameter', {}).get('meters', {}).get('estimated_diameter_max', 0)
        if diameter > 1000:
            return "This NEO is larger than the Eiffel Tower!"
        elif diameter > 500:
            return "This NEO is larger than a football field!"
        else:
            return "This NEO is relatively small compared to most known asteroids."
