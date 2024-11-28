from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

natasha = Blueprint('natasha', __name__)

@natasha.route('/user/<id>', methods=['GET'])
def find_user(id):
    query = f'''
        SELECT username, openToConnect, linkedin, r.review_text, r.rating
        FROM student s
        JOIN review r ON s.id = r.student_id
        WHERE s.id = {id}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
