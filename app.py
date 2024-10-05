from flask import Flask
from orrery.routes import MainRoutes

class FlaskApp:
      def __init__(self):
            self.app = Flask(__name__)
            self.register_blueprint()
            
      def register_blueprint(self):
            main_routes = MainRoutes()
            self.app.register_blueprint(main_routes.blueprint)
            
      def run(self):
            self.app.run(debug=True)
            


if __name__ == "__main__":
      flask_app = FlaskApp()
      flask_app.run()