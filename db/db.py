import os
import psycopg2
import psycopg2.extras
DB_URL = os.environ.get("postgres://dazza:PmtzjyYMXicurxVKanZVq8BkDUgZyqij@dpg-che83i67avja5mbt6uo0-a/videogamedb_458t", "dbname=videogamedb")