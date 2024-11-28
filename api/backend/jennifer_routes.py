from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

jennifer = Blueprint('jennifer', __name__)

# Gets summary data for a specific co-op
@jennifer.route('/trends/<position_id>', methods=['GET'])
def summary_data(position_id):
    query = f'''
        SELECT r.review_id, p.position name, r.rating, r.review_text
        FROM review r
        JOIN position p ON r.position_id = p.id
        WHERE r.position_id = {id}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Returns a specific co-op student (Natasha's 2nd story)
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