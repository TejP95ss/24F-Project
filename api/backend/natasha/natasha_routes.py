from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

natasha = Blueprint('natasha', __name__)

# Gets all reviews for a specific position id (Natasha's 1st story)
@natasha.route('/review/<position_id>', methods=['GET'])
def find_position_reviews(position_id):
    query = f'''
        SELECT id, rating, review_text
        FROM review r
        WHERE position_id = {position_id}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Returns a specific co-op student (Natasha's 2nd story)
@natasha.route('/student/<id>', methods=['GET'])
def find_student(id):
    query = f'''
        SELECT id, username, openToConnect, linkedin, major
        FROM student
        WHERE id = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (id,))
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Returns a list of co op students (Natasha's 2nd story)
@natasha.route('/student', methods=['GET'])
def get_users():
    query = f'''
        SELECT id, username, openToConnect, linkedin, major
        FROM student 
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Adds a user profile and contact information (Natasha's 3rd story)
@natasha.route('/student', methods=['POST'])
def add_user():
    user_data = request.json
    username = user_data['username']
    profileType = user_data['profileType']
    openToConnect = user_data['openToConnect']

    query = f'''
        INSERT INTO student (username, profileType, openToConnect)
        VALUES ({username}, {profileType}, {openToConnect})
    '''
    current_app.logger.info(f'Query: {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query, (username, profileType, openToConnect))
    db.get_db().commit()

    response = make_response("User added successfully!")
    response.status_code = 201
    return response

# Route to edit user's connection preferences (Natasha's 4th story)
@natasha.route('/student/<id>', methods = ['PUT'])
def update_connect(id):
    input = request.json
    connect = input['openToConnect']

    query = f'''
        UPDATE student
        SET openToConnect = {connect}
        WHERE id = %s
        '''
        
    current_app.logger.info(f'Query: {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query, (id,))
    db.get_db().commit()

    response = make_response("Connection preferences successfully updated")
    response.status_code = 200
    return response

# Route to delete a specific review (Natasha's 5th story)
@natasha.route('/review/<id>', methods=['DELETE'])
def delete_review(id):
    query = f'''
        DELETE FROM review
        WHERE id = {id}
    '''
    current_app.logger.info(f'Query: {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Review removed from site successfully")
    response.status_code = 200
    return response

# Route to update an existing review (Natasha's 6th story)
@natasha.route('/review/<id>', methods=['PUT'])
def update_review(id):
    review_data = request.json
    rating = review_data['rating']
    comments = review_data['review_text']

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
