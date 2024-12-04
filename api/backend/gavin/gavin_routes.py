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
        AND s.openToConnect = TRUE;
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
        FROM student s;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Adds a backup application into the log
@gavin.route('/logs_backup/<id>', methods=['PUT'])
def load_backup_app(id):

    query = f'''
        INSERT INTO logs (app_id)
        SELECT {id}
        FROM applications
    '''

    backup_check_query = f"SELECT id FROM applications WHERE id = {id}"
    cursor = db.get_db().cursor()
    cursor.execute(backup_check_query)
    backup_exists = cursor.fetchone()
    
    if not backup_exists:
        current_app.logger.error(f"No backup found with ID: {id}")
        response = make_response(jsonify({"error": f"No backup found with ID: {id}"}))
        response.status_code = 404
        return response

    current_app.logger.info(f'Query: {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    backup_details = cursor.fetchall()

    response = make_response(jsonify(backup_details))
    response.status_code = 200
    return response


# Gets total count of co-ops for each student
@gavin.route('/student/coop_count', methods=['GET'])
def student_total_coops():
    query = f'''
        SELECT s.id, s.username, COUNT(sc.coop_id) AS coop_count
        FROM student s
        LEFT JOIN student_coops sc ON s.id = sc.student_id
        GROUP BY s.id, s.username;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Adds a data analyst to the team (new hire)
@gavin.route('/data_analyst', methods=['POST'])
def hire_analyst():

    analyst_data = request.json
    email = analyst_data['email']
    name = analyst_data['name']
    role = analyst_data['role']

    query = f'''
        INSERT INTO data_analyst (email, name, role)
        VALUES (%s, %s, %s)
        '''
    current_app.logger.info(f'Query: {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query, (email, name, role))
    db.get_db().commit()

    response = make_response("User added successfully!")
    response.status_code = 201
    return response

# Removes the given review from the database
@gavin.route('/review/<id>/remove', methods=['DELETE'])
def delete_review(id):
    query = f'''
        DELETE FROM review
        WHERE id = {id}
    '''

    current_app.logger.info(f'Query: {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Review successfully deleted")
    response.status_code = 200
    return response
