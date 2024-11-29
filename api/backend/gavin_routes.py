from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

gavin = Blueprint('gavin', __name__)

# Gets student ids who are on linkedin and open to connect
@gavin.route('/id', methods=['GET'])
def find_searching_students():
    query = f'''
        SELECT s.id
        FROM student s
        WHERE s.linkedin IS NOT NULL
        AND s.openToConnect = TRUE
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Counts the current number of current student users
@gavin.route('/current_users', methods=['GET'])
def count_student_users():
    query = f'''
        SELECT COUNT(*) AS current_users
        FROM student s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Adds a backup application into the log
@gavin.route('/logs/backup', methods=['PUT'])
def load_backup_app():
    query = f'''
        INSERT INTO logs (app_id)
        SELECT id 
        FROM applications
        WHERE version = 'backup'
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Finds the last 10 submitted applications
@gavin.route('/applications/recent', methods=['GET'])
def ten_recent_applications():
    query = f'''
        SELECT a.name, l.timestamp
        FROM applications a
        JOIN logs l ON a.id = l.app_id
        ORDER BY l.timestamp DESC
        LIMIT 10
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Finds all student IDs with a valid profile
@gavin.route('/student/id/profile', methods=['GET'])
def list_student_profile_ids():
    query = f'''
        SELECT id
        FROM student
        WHERE profileType IS NOT NULL
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response