CREATE DATABASE videogame_db;
\c videogame_db

CREATE TABLE games(
  id SERIAL PRIMARY KEY,
  name TEXT,
  image_url TEXT
);

INSERT INTO games(name, image_url)
VALUES
  ('Super Mario Bros', 'https://e.snmc.io/lk/l/x/e214620b373226ce2d41f17eda1c369c/9224196'),
  ('Doom', 'https://image.api.playstation.com/vulcan/ap/rnd/202009/2406/m3Ko6r12QZBY6n9JfyfsyXTn.png');

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT
);

ALTER TABLE users ADD COLUMN password_digest TEXT;

CREATE TABLE likes(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  game_id INTEGER
);

CREATE TABLE comments(
  id SERIAL PRIMARY KEY,
  game_id INTEGER,
  user_id INTEGER,
  comment TEXT
);