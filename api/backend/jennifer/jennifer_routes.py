from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

jennifer = Blueprint('jennifer', __name__)

# Gets summary data for a specific co-op (Jennifer's 1st story)
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

# Gets recommended skills and majors for a given co-op (Jennifer's 2nd story)
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

# Gets the most common skills and their review counts (Jennifer's 3rd story)
@jennifer.route('/skills/common', methods=['GET'])
def get_common_skills():
    query = '''
        SELECT s.name AS skill_name, COUNT(DISTINCT r.id) AS review_count
        FROM skill s
        JOIN review_skills rs ON s.id = rs.skill_id
        JOIN review r ON rs.review_id = r.id
        GROUP BY s.name
        ORDER BY review_count DESC;
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Gets average rating and review count for each co-op position (Jennifer's 4th story)
@jennifer.route('/positions/ratings', methods=['GET'])
def get_position_ratings():
    query = '''
        SELECT c.name, cp.title,
              AVG(r.rating) AS avg_rating,
              COUNT(r.id) AS review_count
        FROM company c
        JOIN coop_position cp ON c.id = cp.company_id
        LEFT JOIN review r ON cp.id = r.position_id
        GROUP BY c.name, cp.title;
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Gets average satisfaction for each company by industry (Jennifer's 5th story)
@jennifer.route('/companies/satisfaction', methods=['GET'])
def get_company_satisfaction():
    query = '''
        SELECT c.name, c.industry, AVG(r.rating) AS avg_satisfaction
        FROM company c
        JOIN coop_position cp ON c.id = cp.company_id
        JOIN review r ON cp.id = r.position_id
        GROUP BY c.name, c.industry
        ORDER BY avg_satisfaction DESC;
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Gets the student count for each co-op position (Jennifer's 6th story)
@jennifer.route('/positions/students', methods=['GET'])
def get_position_student_counts():
    query = '''
        SELECT cp.title, COUNT(DISTINCT sc.student_id) AS student_count
        FROM coop_position cp
        JOIN student_coops sc ON cp.id = sc.coop_id
        GROUP BY cp.title
        ORDER BY student_count DESC;
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response