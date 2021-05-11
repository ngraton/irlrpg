import functools

from flask import (
  Blueprint, flash, g, request, session, jsonify
)

from . import db

bp = Blueprint('quest', __name__ )

@bp.route('/quest', methods=('GET', 'POST'))
def quest_return():
    quest_db = db.get_db()
    if request.method == 'POST':
        hero_id = request.form['hero_id']
        title = request.form['title']
        error = None

        if not hero_id:
            error = 'Hero is required.'
        elif not title:
            error = 'Quest title is required.'

        if error is None:
            quest_db.execute(
                'INSERT INTO quest (hero_id, title) VALUES (?, ?)', (hero_id, title,)
            )
            quest_db.commit()
            return jsonify({'status': 'success'})

    quest = quest_db.execute(
        'SELECT * FROM quest WHERE hero_id = ?', (request.args['hero_id'],)
    ).fetchall()

    return jsonify(quest)