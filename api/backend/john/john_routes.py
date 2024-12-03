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

# Route to add a new review for a specific co-op position(John's 1st story)
@john.route('/reviews/<id>', methods=['POST'])
def add_review(id):
    review_data = request.json
    rating = review_data['rating']
    comments = review_data['review_text']
    user_id = review_data['student_id']

    position_check_query = f"SELECT id FROM coop_position WHERE id = {id}"
    cursor = db.get_db().cursor()
    cursor.execute(position_check_query)
    position_exists = cursor.fetchone()
    
    if not position_exists:
        current_app.logger.error(f"No position found with ID: {id}")
        response = make_response(jsonify({"error": f"No position found with ID: {id}"}))
        response.status_code = 404
        return response

    query = f'''
        INSERT INTO review (rating, review_text, student_id, position_id)
        VALUES ({rating}, '{comments}', {user_id}, {id})
    '''
    current_app.logger.info(f'Query: {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Review added successfully")
    response.status_code = 201
    return response


# Route to add a new skill to a user's profile(John's 5th Story)
@john.route('/user/<id>/skills', methods=['POST'])
def add_user_skill(id):
    skill_data = request.json
    skill_id = skill_data['skill_id']

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

# Route to update an existing review
@john.route('/reviews/<id>', methods=['PUT'])
def update_review(id):
    review_data = request.json
    rating = review_data['rating']
    comments = review_data['review_text']

    review_check_query = f"SELECT id FROM review WHERE id = {id}"
    cursor = db.get_db().cursor()
    cursor.execute(review_check_query)
    review_exists = cursor.fetchone()
    
    if not review_exists:
        current_app.logger.error(f"No review found with ID: {id}")
        response = make_response(jsonify({"error": f"No review found with ID: {id}"}))
        response.status_code = 404
        return response

    query = f'''
        UPDATE review
        SET rating = {rating}, review_text = '{comments}'
        WHERE id = {id}
    '''

    current_app.logger.info(f'Query: {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Review successfully updated")
    response.status_code = 200
    return response