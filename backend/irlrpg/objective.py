import functools

from flask import (
  Blueprint, flash, g, request, session
)

from . import db

bp = Blueprint('objective', __name__ )

@bp.route('/objective', methods=('GET', 'POST'))
    def charcter_return():
        objective_db = db.get_db()
        if request.method == 'POST':
            quest_id = request.form['quest_id']
            description = request.form['description']
            completed = request.form['completed']

            error = None

            if not quest_id:
                error = 'quest is required.'
            if not description:
              error = 'descroption is requried'


            if error is None:
                objective_db.execute(
                    'INSERT INTO objective (quest_id, decription, completed) VALUES (?, ?, ?)', (quest_id, description, completed,)
                )
                objective_db.commit()
                return jsonify({'status': 'success'})

        return jsonify(objective_db.execute(
            'SELECT * FROM objective'
        ).fetchall())