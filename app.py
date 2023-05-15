from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
from flask import Flask, redirect, request
from flask import render_template
import os
from db.db import sql

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/users/new')
def signup():
  return render_template('/users/new.html')

@app.route('/users', methods=["POST"])
def users_create():
  first_name = request.form.get("first_name")
  last_name = request.form.get("last_name")
  email = request.form.get("email")

  sql('INSERT INTO users(first_name, last_name, email) VALUES(%s, %s, %s) RETURNING *', [first_name, last_name, email])
  return redirect('/')


@app.route('/sessions/new')
def login():
  return render_template('/sessions/new.html')