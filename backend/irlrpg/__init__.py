import os, json

from flask import Flask, jsonify, request


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'irlrpg.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import (
        quest,
        character,
        objective
    )
    app.register_blueprint(quest.bp)
    app.register_blueprint(character.bp)
    app.register_blueprint(objective.bp)

    from . import db
    db.init_app(app)

    return app