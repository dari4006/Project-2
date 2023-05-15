from flask import render_template, request, redirect, session
from models.games import all_foods, get_food, create_food, update_food, delete_food, like_food
from services.session_info import current_user

def index():
  foods = all_foods()
  return render_template('foods/index.html', foods=foods, current_user=current_user())

def new():
  return render_template('foods/new.html')

def create():
  name = request.form.get('name')
  image_url = request.form.get('image_url')
  create_food(name, image_url)
  return redirect('/')

def edit(id):
  food = get_food(id)
  return render_template('foods/edit.html', food=food)

def update(id):
  name = request.form.get('name')
  image_url = request.form.get('image_url')
  update_food(id, name, image_url)
  return redirect('/')

def delete(id):
  delete_food(id)
  return redirect('/')

def like(id):
  like_food(id, session['user_id'])
  return redirect('/')