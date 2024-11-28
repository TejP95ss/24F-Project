from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

natasha = Blueprint('natasha', __name__)

# Gets all reviews for a specific position id (Natasha's 1st story)
@natasha.route('/review/position/<position_id>', methods=['GET'])
def find_position_reviews(id):
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

# Adds a user profile and contact information (Natasha's 3rd story)
@natasha.route('/user/<id>', methods=['POST'])
def add_user(id):
    user_data = request.json
    username = user_data['username']
    profileType = user_data['profileType']
    openToConnect = user_data['openToConnect']

    query = f'''
        INSERT INTO user (username, profileType, openToConnect)
        VALUES ({id}, {skill_id}, {openToConnect})
    '''
    current_app.logger.info(f'Query: {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("User added successfully!")
    response.status_code = 201
    return response

# Returns a list of co op students (Natasha's 2nd and 4th story)
@natasha.route('/user', methods=['GET'])
def get_users():
    query = f'''
        SELECT username, openToConnect, linkedin, major
        FROM student 
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Route to delete a review for a user
@john.route('/review/<id>', methods=['DELETE'])
def delete_review(id):
    review_data = request.json
    review_id = review_data['id']

    query = f'''
        DELETE FROM review
        WHERE review_id = {id} 
    '''
    current_app.logger.info(f'Query: {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Review removed from site successfully")
    response.status_code = 200
    return response
