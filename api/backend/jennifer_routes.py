from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

jennifer = Blueprint('jennifer', __name__)

# Gets summary data for a specific co-op
@jennifer.route('/trends/<position_id>', methods=['GET'])
def summary_data(id):
    query = f'''
        SELECT c.name, cp.title, AVG(r.rating) AS avg_rating
        FROM coop_position cp
        JOIN company c ON cp.company_id = c.id
        JOIN review r ON r.position_id = cp.id
        WHERE r.position_id = {id}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Gets recommended skills and majors for a co op
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