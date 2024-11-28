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

# Gets recommended skills and majors for a given co-op
@jennifer.route('/position/<position_id>', methods=['GET'])
def coop_skills_info(id):
    query = f'''
        SELECT cp.title, s.name AS skill_name, COUNT(*) AS skill_frequency, st.major
        FROM coop_position cp
        JOIN review r ON r.position_id = cp.id
        JOIN review_skills rs ON r.id = rs.review_id
        JOIN skill s ON rs.skill_id = s.id
        WHERE cp.id = {id}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response