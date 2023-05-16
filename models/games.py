from db.db import sql

def all_games():
  return sql('SELECT * FROM games ORDER BY id')

def get_games(id):
  games = sql("SELECT * FROM games WHERE id = %s", [id])
  return games[0]

def create_game(name, image_url):
  sql('INSERT INTO games(name, image_url) VALUES(%s, %s) RETURNING *', [name, image_url])

def update_game(id, name, image_url):
  sql('UPDATE games SET name=%s, image_url=%s WHERE id=%s RETURNING *', [name, image_url, id])

def delete_game(id):
  sql('DELETE FROM games WHERE id=%s RETURNING *', [id])

def like_game(game_id, user_id):
  sql("INSERT INTO likes(user_id, game_id) VALUES(%s, %s) RETURNING *", [user_id, game_id])