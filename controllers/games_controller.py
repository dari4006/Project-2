from flask import render_template, request, redirect, session
from models.games import all_games, get_games, create_game, update_game, delete_game, like_game, create_newcomment
from services.session_info import current_user

def index():
  games = all_games()
  return render_template('games/index.html', games=games, current_user=current_user())

def new():
  return render_template('games/new.html')

def create():
  name = request.form.get('name')
  image_url = request.form.get('image_url')
  create_game(name, image_url)
  return redirect('/')

def edit(id):
  game = get_games(id)
  return render_template('games/edit.html', game=game)

def update(id):
  name = request.form.get('name')
  image_url = request.form.get('image_url')
  update_game(id, name, image_url)
  return redirect('/')

def delete(id):
  delete_game(id)
  return redirect('/')

def like(id):
  like_game(id, session['user_id'])
  return redirect('/')

def create_comment(id):
  comment = request.form.get('comments')
  create_newcomment(id, session['user_id'], comment)
  return redirect('/')
