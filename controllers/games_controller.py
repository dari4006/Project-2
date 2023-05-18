from flask import render_template, request, redirect, session
from models.games import all_games, get_games, create_game, update_game, delete_game, like_game, create_comment, comments_by_game
from services.session_info import current_user

def index():
  games = all_games()
  all_comments = []
  for game in games:
    all_comments.append(comments_by_game(game['id']))
  for i in range(len(games)):
    games[i]['comments'] = []
    for comment in all_comments[i]:
      games[i]['comments'].append(comment['comment'])
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

def comment(id):
  comment = request.form.get('comments')
  create_comment(id, session['user_id'], comment)
  return redirect('/')

