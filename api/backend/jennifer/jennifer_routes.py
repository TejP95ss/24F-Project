from flask import Blueprint, request, jsonify, make_response
from backend.db_connection import db

jennifer = Blueprint('jennifer', __name__)

# Gets summary data for a specific co-op (Jennifer's 1st story)
@jennifer.route('/trends/<position_id>', methods=['GET'])
def get_coop_summary(position_id):
    query = '''
        SELECT c.name, cp.title, AVG(r.rating) AS avg_rating
        FROM coop_position cp
        JOIN company c ON cp.company_id = c.id
        JOIN review r ON r.position_id = cp.id
        WHERE cp.id = %s
        GROUP BY c.name, cp.title;
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (position_id,))
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Gets the most common skills and their review counts (Jennifer's 2nd story)
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

# Adds a new task (Jennifer's 3rd story)
@jennifer.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    query = '''
        INSERT INTO tasks (report_id, created_by, name, status, assigned_to, timestamp, description)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    values = (
        data['report_id'],
        data['created_by'],
        data['name'],
        data['status'],
        data['assigned_to'],
        data['timestamp'],
        data['description']
    )
    cursor = db.get_db().cursor()
    cursor.execute(query, values)
    db.get_db().commit()

    response = make_response(jsonify({"message": "Task added successfully!"}))
    response.status_code = 201
    return response

# Updates the status and description of a task (Jennifer's 4th story)
@jennifer.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    query = '''
        UPDATE tasks
        SET status = %s, description = %s
        WHERE id = %s
    '''
    values = (data['status'], data['description'], task_id)
    cursor = db.get_db().cursor()
    cursor.execute(query, values)
    db.get_db().commit()

    response = make_response(jsonify({"message": "Task updated successfully!"}))
    response.status_code = 200
    return response

# Deletes a specific task (Jennifer's 5th story)
@jennifer.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    query = '''
        DELETE FROM tasks WHERE id = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (task_id,))
    db.get_db().commit()

    response = make_response(jsonify({"message": "Task deleted successfully!"}))
    response.status_code = 200
    return response

# Gets average satisfaction for each company by industry (Jennifer's 6th story)
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
