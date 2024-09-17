#!/usr/bin/env python3
from flask import Blueprint
from ..models.maze import Maze

app_views = Blueprint("app_views", __name__, url_prefix='')
maze : (Maze | None) = None

from .index import *