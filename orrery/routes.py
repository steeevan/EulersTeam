import requests
from flask import Blueprint, render_template, jsonify, request
from datetime import datetime, timedelta

class MainRoutes:
    def __init__(self):
        # Create a Blueprint for the main routes
        self.blueprint = Blueprint('main',__name__)
        self.api_key = "Xgfq91jzvo3E3uo9cDFYW7Cw9fYNB6vz5g8RVkJJ"
        self.start_month = input("Please enter the month you would like to start in as the abbreviated 3 letter version of the month:")
        self.start_day = input("Please enter the day you would like to start in as DD format:")
        self.start_year = input("Please enter the year you would like to start in as YYYY format:")
        self.end_month = input("Please enter the month you would like to start in as the abbreviated 3 letter version of the month:")
        self.end_day = input("Please enter the day you would like to start in as DD format:")
        self.end_year = input("Please enter the year you would like to start in as YYYY format:")
        self.d1 = datetime.strptime(self.start_day+" "+self.start_month.lower()+" "+self.start_year, '%d %b %Y')
        self.d2 = datetime.strptime(self.end_day+" "+self.end_month.lower()+" "+self.end_year, '%d %b %Y') # date is 20th jun 2022
        self.diff = self.d2 - self.d1

        self.weeks = ((self.diff.days) // 7) - 1
        self.extra_days = (self.diff.days) % 7

        if self.start_month.lower() == "jan":
            self.start_month = "01"
        elif self.start_month.lower() == "feb":
            self.start_month =  "02"
        elif self.start_month.lower() == "mar":
            self.start_month =  "03"
        elif self.start_month.lower() == "apr":
            self.start_month =  "04"
        elif self.start_month.lower() == "may":
            self.start_month =  "05"
        elif self.start_month.lower() == "jun":
            self.start_month =  "06"
        elif self.start_month.lower() == "jul":
            self.start_month =  "07"
        elif self.start_month.lower() == "aug":
            self.start_month =  "08"
        elif self.start_month.lower() == "sep":
            self.start_month =  "09"
        elif self.start_month.lower() == "oct":
            self.start_month =  "10"
        elif self.start_month.lower() == "nov":
            self.start_month =  "11"
        elif self.start_month.lower() == "dec":
            self.start_month =  "12"
        else:
            pass
        self.counter = 0
        self.start_day = int(self.start_day)
        self.start_month = int(self.start_month)
        self.start_year = int(self.start_year)
        self.data = {}
        for i in range(self.weeks):
            if self.counter % 52 ==0:
                self.start_year +=1
            elif self.counter % 4 == 0:
                self.start_month +=1
            else:
                self.start_date = f"{str(self.start_year).zfill(2)}-{str(self.start_month).zfill(2)}-{str(self.start_day).zfill(2)}"
                self.end_date = ""
                self.url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={self.start_date}&end_date={self.end_date}&api_key={self.api_key}"
                self.responsey = requests.get(self.url)
                self.data = {**self.responsey.json(),**self.data}
                self.start_day +=7
            self.counter +=1

                

        self.register_routes()
        print(self.data)



    def register_routes(self):
        # define route handlers
        @self.blueprint.route('/')
        def index():
            return render_template('index.html')
        
test = MainRoutes()
