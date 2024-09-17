from flask import jsonify, request, abort
from . import app_views
from ..models.maze import Maze
from . import maze
import json
import networkx as nx

@app_views.route('/', methods=['GET'], strict_slashes=False)
def home():
    return jsonify({'Message': 'Welcome to path finder simple API'}), 200

@app_views.route('/generate-maze', methods=['GET'], strict_slashes=False)
def generate():
    global maze
    rows = request.args.get('rows')
    cols = request.args.get('cols')
    difficulty = request.args.get('difficulty')
    if not rows:
        rows = 20
    if not cols:
        cols = 20
    if not difficulty:
        difficulty = 'Normal'
    rows = int(rows)
    cols = int(cols)
    maze = Maze(rows, cols, difficulty)
    maze.drawing_nodes()
    return jsonify({'Status': 'Maze was generated'}), 200

@app_views.route('/solve-maze', methods=['GET'], strict_slashes=False)
def solve():
    global maze
    if not maze:
        abort(409)
    maze.path = maze.solve_maze()
    json_list_path = json.dumps([list(item) for item in maze.path])
    maze.drawing_nodes()
    return jsonify({'path': json_list_path}), 200
