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

# Updates the linkedin URL for the student's profile
@john.route('/user/<id>/linkedin', methods=['PUT'])
def update_linkedin_url(id):
    data = request.json
    id_check = f"SELECT id FROM student WHERE id = {id}"
    cursor = db.get_db().cursor()
    cursor.execute(id_check)
    exists = cursor.fetchone()
    
    if not exists:
        current_app.logger.error(f"{id} is not associated with student id: {id}")
        response = make_response(jsonify({"error": f"{id} is not associated with student id: {id}"}))
        response.status_code = 404
        return response   
    
    linkedin_url = data['linkedin_url']

    query = f"UPDATE student SET linkedin = '{linkedin_url}' WHERE id = {id}"

    cursor = db.get_db().cursor()
    try:
        cursor.execute(query)
        db.get_db().commit()

        response = make_response("LinkedIn URL updated successfully")
        response.status_code = 200
    except Exception as e:
        current_app.logger.error(f"Error updating LinkedIn URL: {str(e)}")
        response = make_response(jsonify({"error": "Failed to update LinkedIn URL"}), 500)
    return response

@john.route('/students/open_to_connect', methods=['GET'])
def get_students_open_to_connect():
    query = """
        SELECT id, full_name, linkedin
        FROM student
        WHERE openToConnect = 1
    """
    cursor = db.get_db().cursor()
    try:
        cursor.execute(query)
        students = cursor.fetchall()
        if not students:
            response = make_response(jsonify({"message": "No students found who are open to connect"}), 404)
            return response
        response = make_response(jsonify(students))
        response.status_code = 200
    except Exception as e:
        current_app.logger.error(f"Error fetching students open to connect: {str(e)}")
        response = make_response(jsonify({"error": "Failed to fetch students"}), 500)
    return response
