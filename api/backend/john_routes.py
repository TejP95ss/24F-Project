from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

john = Blueprint('john', __name__)

# Route to get detailed information about a specific co-op position(John's 6th story)
@john.route('/positions/<id>', methods=['GET'])
def get_position_details(id):
    query = f'''
        SELECT id, title, company_id, hourly_wage, workload, description
        FROM Co_op_Positions
        WHERE id = {id}
    '''
    current_app.logger.info(f'Query: {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    position_details = cursor.fetchall()

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

    query = f'''
        INSERT INTO Reviews (rating, review_text, student_id, position_id)
        VALUES ({rating}, '{comments}', {user_id}, {id})
    '''
    current_app.logger.info(f'Query: {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Review added successfully")
    response.status_code = 201
    return response
