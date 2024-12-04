from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

john = Blueprint('john', __name__)

# Route to get detailed information about a specific co-op position(John's 6th story)
@john.route('/positions/<id>', methods=['GET'])
def get_position_details(id):
    query = f'''
        SELECT id, title, company_id, hourly_wage, workload, description
        FROM coop_position
        WHERE id = {id}
    '''
    current_app.logger.info(f'Query: {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    position_details = cursor.fetchall()

    if not position_details:
        current_app.logger.error(f"No position found with ID: {id}")
        response = make_response(jsonify({"error": f"No position found with ID: {id}"}))
        response.status_code = 404
        return response

    response = make_response(jsonify(position_details))
    response.status_code = 200
    return response

# Route to add a new skill to a user's profile(John's 5th Story)
@john.route('/user/<id>/skills', methods=['POST'])
def add_user_skill(id):
    skill_data = request.json
    skill_id = skill_data['skill_id']

    student_and_skill = f"""
    SELECT 'student' AS type FROM student WHERE id = {id}
    UNION
    SELECT 'skill' AS type FROM skill WHERE id = {skill_id};
    """
    cursor = db.get_db().cursor()
    cursor.execute(student_and_skill)
    exists = cursor.fetchall()
    
    types_found = {row['type'] for row in exists}
    
    if 'student' not in types_found or 'skill' not in types_found:
        response = make_response(jsonify({"error": f"Invalid student id or skill id given"}))
        response.status_code = 404
        return response
    
    query = f'''
        INSERT INTO student_skills (student_id, skill_id)
        VALUES ({id}, {skill_id})
    '''
    current_app.logger.info(f'Query: {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Skill added to user's profile successfully")
    response.status_code = 201
    return response

# Route to delete a skill from a user's profile
@john.route('/user/<id>/skills', methods=['DELETE'])
def delete_user_skill(id):
    skill_data = request.json
    skill_id = skill_data['skill_id']

    student_skill_check = f"SELECT student_id FROM student_skills WHERE student_id = {id} AND skill_id = {skill_id}"
    cursor = db.get_db().cursor()
    cursor.execute(student_skill_check)
    exists = cursor.fetchone()
    
    if not exists:
        current_app.logger.error(f"{skill_id} is not associated with student id: {id}")
        response = make_response(jsonify({"error": f"{skill_id} is not associated with student id: {id}"}))
        response.status_code = 404
        return response    

    query = f'''
        DELETE FROM student_skills
        WHERE student_id = {id} AND skill_id = {skill_id}
    '''
    current_app.logger.info(f'Query: {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Skill removed from user's profile successfully")
    response.status_code = 200
    return response
