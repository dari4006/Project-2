from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
from flask import Flask, redirect
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')