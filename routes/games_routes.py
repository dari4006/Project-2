from flask import Blueprint
from controllers.games_controller import index, new, create, edit, update, delete, like

games_routes = Blueprint('games_routes', __name__)

games_routes.route('')(index)
games_routes.route('/new')(new)
games_routes.route('', methods=['POST'])(create)
games_routes.route('/<id>/edit')(edit)
games_routes.route('/<id>', methods=["POST"])(update)
games_routes.route('/<id>/delete', methods=["POST"])(delete)
games_routes.route('/<id>/likes', methods=["POST"])(like)