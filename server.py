from flask_app import app
from flask_app.controllers import users_controller, stories_controller, likes_controller

if __name__ == "__main__":
    app.run(debug=True)