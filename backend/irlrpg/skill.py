import functools

from flask import (
  Blueprint, flash, g, request, session
)

from . import db

bp = Blueprint('skill', __name__ )