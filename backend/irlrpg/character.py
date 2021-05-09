import functools

from flask import (
  Blueprint, flash, g, request, session
)

from . import db

bp = Blueprint('character', __name__ )

@bp.route('/character', methods=('GET', 'POST'))
    def charcter_return():
        character_db = db.get_db()
        if request.method == 'POST':
            username = request.form['username']
            error = None

            if not username:
                error = 'Username is required.'
            elif character_db.execute(
                'SELECT id FROM user WHERE username = ?', (username,)
            ).fetchone() is not None:
                error = 'Username is taken.'

            if error is None:
                character_db.execute(
                    'INSERT INTO user (username) VALUES (?)', (username,)
                )
                character_db.commit()
                return jsonify({'status': 'success'})

        return jsonify(character_db.execute(
            'SELECT * FROM user'
        ).fetchall())