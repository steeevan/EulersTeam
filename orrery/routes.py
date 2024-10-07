import requests
from flask import Blueprint, render_template, jsonify, request
from datetime import datetime, timedelta
import json
from datetime import datetime, timedelta
import json

class MainRoutes:
    def __init__(self):
        # Create a Blueprint for the main routes
        self.blueprint = Blueprint('main',__name__)
        self.register_routes()



    def register_routes(self):
        # define route handlers
        @self.blueprint.route('/')
        def index():
            return render_template('index.html')
        @self.blueprint.route('/aboutus')
        def aboutus():
            return render_template('aboutUS.html')
        @self.blueprint.route('/neopage')
        def neopage():
            return render_template('neopage.html',json_neos_data=neos_data)
        
        @self.blueprint.route('/orbitsim')
        def orbital():
            return render_template('orbit_simulation.html')
        @self.blueprint.route('/facts')
        def facts():
              return render_template('facts.html')
        @self.blueprint.route('/back')
        def back(): 
            return render_template('index.html')
        
        @self.blueprint.route('/neptune')
        def neptune(): 
            return render_template('neptune.html')
        @self.blueprint.route('/uranus')
        def uranus(): 
            return render_template('uranus.html')
        @self.blueprint.route('/saturn')
        def saturn(): 
            return render_template('saturn.html')
        @self.blueprint.route('/jupiter')
        def jupiter(): 
            return render_template('jupiter.html')
        @self.blueprint.route('/mars')
        def mars(): 
            return render_template('mars.html')
        @self.blueprint.route('/earth')
        def earth(): 
            return render_template('earth.html')
        @self.blueprint.route('/venus')
        def venus(): 
            return render_template('venus.html')
        @self.blueprint.route('/mercury')
        def mercury(): 
            return render_template('mercury.html')
#test = MainRoutes()

api_key = "Xgfq91jzvo3E3uo9cDFYW7Cw9fYNB6vz5g8RVkJJ"
'''
start_month = input("Please enter the month you would like to start in as the abbreviated 3 letter version of the month:")
start_day = input("Please enter the day you would like to start in as DD format:")
start_year = input("Please enter the year you would like to start in as YYYY format:")
end_month = input("Please enter the month you would like to end in as the abbreviated 3 letter version of the month:")
end_day = input("Please enter the day you would like to end in as DD format:")
end_year = input("Please enter the year you would like to end in as YYYY format:")
d1 = datetime.strptime(start_day+" "+start_month.lower()+" "+start_year, '%d %b %Y')
d2 = datetime.strptime(end_day+" "+end_month.lower()+" "+end_year, '%d %b %Y') # date is 20th jun 2022
diff = d2 - d1

weeks = ((diff.days) // 7) - 1
extra_days = (diff.days) % 7

if start_month.lower() == "jan":
    start_month = "01"
elif start_month.lower() == "feb":
    start_month =  "02"
elif start_month.lower() == "mar":
    start_month =  "03"
elif start_month.lower() == "apr":
    start_month =  "04"
elif start_month.lower() == "may":
    start_month =  "05"
elif start_month.lower() == "jun":
    start_month =  "06"
elif start_month.lower() == "jul":
    start_month =  "07"
elif start_month.lower() == "aug":
    start_month =  "08"
elif start_month.lower() == "sep":
    start_month =  "09"
elif start_month.lower() == "oct":
    start_month =  "10"
elif start_month.lower() == "nov":
    start_month =  "11"
elif start_month.lower() == "dec":
    start_month =  "12"
else:
    pass
counter = 0
start_dayy = int(start_day)
start_monthy = int(start_month)
start_yeary = int(start_year)
data = {}
for i in range(weeks):
    if counter == 0:
        start_date = f"{str(start_yeary).zfill(2)}-{str(start_monthy).zfill(2)}-{str(start_dayy).zfill(2)}"
        end_date = ""
        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}"
        responsey = requests.get(url)
        data = {**responsey.json(),**data}
        start_dayy +=7
    elif counter % 52 ==0:
        start_yeary +=1
    elif counter % 4 == 0:
        start_monthy +=1
    else:
        start_date = f"{str(start_yeary).zfill(2)}-{str(start_monthy).zfill(2)}-{str(start_dayy).zfill(2)}"
        end_date = ""
        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}"
        responsey = requests.get(url)
        data = {**responsey.json(),**data}
        start_dayy +=7
    counter +=1
        
'''
start_month = "jan" #input("Please enter the month you would like to start in as the abbreviated 3 letter version of the month:")
start_day = "01"#input("Please enter the day you would like to start in as DD format:")
start_year = "2024"#input("Please enter the year you would like to start in as YYYY format:")
end_month = "oct"#input("Please enter the month you would like to end in as the abbreviated 3 letter version of the month:")
end_day = "05"#input("Please enter the day you would like to end in as DD format:")
end_year = "2024"#input("Please enter the year you would like to end in as YYYY format:")
d1 = datetime.strptime(start_day+" "+start_month.lower()+" "+start_year, '%d %b %Y')
d2 = datetime.strptime(end_day+" "+end_month.lower()+" "+end_year, '%d %b %Y') # date is 20th jun 2022
diff = d2 - d1

weeks = ((diff.days) // 7) - 1
extra_days = (diff.days) % 7

if start_month.lower() == "jan":
    start_month = "01"
elif start_month.lower() == "feb":
    start_month =  "02"
elif start_month.lower() == "mar":
    start_month =  "03"
elif start_month.lower() == "apr":
    start_month =  "04"
elif start_month.lower() == "may":
    start_month =  "05"
elif start_month.lower() == "jun":
    start_month =  "06"
elif start_month.lower() == "jul":
    start_month =  "07"
elif start_month.lower() == "aug":
    start_month =  "08"
elif start_month.lower() == "sep":
    start_month =  "09"
elif start_month.lower() == "oct":
    start_month =  "10"
elif start_month.lower() == "nov":
    start_month =  "11"
elif start_month.lower() == "dec":
    start_month =  "12"
else:
    pass
counter = 0
start_dayy = int(start_day)
start_monthy = int(start_month)
start_yeary = int(start_year)
data = {}
for i in range(weeks):
    if counter == 0:
        start_date = f"{str(start_yeary).zfill(2)}-{str(start_monthy).zfill(2)}-{str(start_dayy).zfill(2)}"
        end_date = ""
        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}"
        responsey = requests.get(url)
        data = {**responsey.json(),**data}
        start_dayy +=7
    elif counter % 365 ==0:
        start_yeary +=1
    elif counter % 28 == 0:
        start_monthy +=1
    else:
        start_date = f"{str(start_yeary).zfill(2)}-{str(start_monthy).zfill(2)}-{str(start_dayy).zfill(2)}"
        end_date = ""
        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}"
        responsey = requests.get(url)
        data = {**responsey.json(),**data}
        start_dayy +=7
    counter +=1
        

# Extract relevant NEO data

'''

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
'''

# Extract relevant NEO data
# Ensure that 'near_earth_objects' is a list and each element is a dictionary
# Ensure that 'near_earth_objects' is a dictionary with date keys
neos_data = []
if isinstance(data.get('near_earth_objects'), dict):
    for date_key, neos in data['near_earth_objects'].items():
        if isinstance(neos, list):
            for neo in neos:
                if isinstance(neo, dict):
                    neo_entry = {
                        'name': neo.get('name', 'Unknown'),
                        'id': neo.get('id', 'Unknown'),
                        'estimated_diameter': neo.get('estimated_diameter', {}).get('meters', {}).get('estimated_diameter_max', 'Unknown'),
                        'orbiting_body': neo.get('orbiting_body', 'Unknown')
                    }
                    
                    if isinstance(neo.get('close_approach_data'), list) and neo['close_approach_data']:
                        neo_entry['close_approach_data'] = neo['close_approach_data'][0]
                        
                        # Get orbiting_body from close_approach_data
                        neo_entry['orbiting_body'] = neo['close_approach_data'][0].get('orbiting_body', 'Unknown')
                    else:
                        neo_entry['close_approach_data'] = {}  # Empty data if not present
                        neo_entry['orbiting_body'] = 'Unknown'  # No close approach data, set orbiting_body to 'Unknown'
                    
                    neos_data.append(neo_entry)
                    
# Sort NEOs by distance from Earth, only if 'close_approach_data' exists and contains valid data
neos_data.sort(key=lambda x: float(x['close_approach_data'].get('miss_distance', {}).get('kilometers', float('inf'))))
'''
# Print only the "name" of each NEO
for neo in neos_data:
    print(f"name: {neo['name']}, id: {neo['id']}, and estimated_diameter: {neo['estimated_diameter']}")

print(f"Total NEOs: {len(neos_data)}")
'''
'''
'''
'''
self.start_day = int(self.start_day)
self.start_month = int(self.start_month)
self.start_year = int(self.start_year)
self.register_routes()
self.sec = 0
for key in self.data:
    if self.sec % 365 ==0:
        self.start_yeary +=1
    elif self.sec % 12 == 0:
        self.start_monthy +=1
    else:
        self.start_dayy +=1
    try:
        print(self.data["near_earth_objects"][f"{str(self.start_year).zfill(2)}-{str(self.start_month).zfill(2)}-{str(self.start_day).zfill(2)}"]["name"])
    except:
        pass
    self.sec += 1
    self.start_day +=1

'''