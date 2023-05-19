from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
from flask import Flask, redirect, request
from flask import render_template
import os
from db.db import sql
from routes.games_routes import games_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes
import requests
requests.get(f"http://omdbapi.com?apikey={os.environ.get('OMDB_API_KEY')}&t=jaws").json()


SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "test key")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(games_routes, url_prefix='/games')
app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')

@app.route('/')
def index():
  return redirect('/games')



#