import requests
from flask import Blueprint, render_template, jsonify, request

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
        @self.blueprint.route("/index")
        def back():
              return render_template('index.html')