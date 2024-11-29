from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

gavin = Blueprint('gavin', __name__)

# Gets student ids who are on linkedin and open to connect
@gavin.route('/id/<id>', methods=['GET'])
def find_searching_students(id):
    query = f'''
        SELECT s.id
        FROM student s
        WHERE s.linkedin IS NOT NULL
        AND s.openToConnect = TRUE
        WHERE s.id = {id}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response