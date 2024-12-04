from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

jennifer = Blueprint('jennifer', __name__)

# Route to get aggregated trends by industry (Jennifer's 1st Story)
@jennifer.route('/trends', methods=['GET'])
def get_aggregated_trends():
    query = '''
        SELECT industry, skill_alignments, career_alignments, satisfaction_alignments
        FROM trends
    '''
    cursor = db.get_db().cursor(dictionary=True)  # Use dictionary=True for easy JSON conversion
    current_app.logger.info(f'Executing query: {query}')
    try:
        cursor.execute(query)
        trends = cursor.fetchall()
        if not trends:
            response = make_response(jsonify({"message": "No trends found"}), 404)
        else:
            response = make_response(jsonify(trends), 200)
    except Exception as e:
        current_app.logger.error(f"Error fetching trends: {str(e)}")
        response = make_response(jsonify({"error": "Failed to fetch trends"}), 500)
    return response

# Route to add a new trend (Jennifer's 2nd Story)
@jennifer.route('/trends', methods=['POST'])
def add_new_trend():
    data = request.json
    query = f'''
        INSERT INTO trends (industry, skill_alignments, career_alignments, satisfaction_alignments)
        VALUES ('{data['industry']}', '{data['skill_alignments']}', '{data['career_alignments']}', '{data['satisfaction_alignments']}')
    '''
    cursor = db.get_db().cursor()
    current_app.logger.info(f'Query: {query}')
    try:
        cursor.execute(query)
        db.get_db().commit()
        response = make_response(jsonify({"message": "New trend added successfully"}), 201)
    except Exception as e:
        current_app.logger.error(f"Error adding new trend: {str(e)}")
        response = make_response(jsonify({"error": "Failed to add trend"}), 500)
    return response

# Route to update a trend (Jennifer's 3rd Story)
@jennifer.route('/trends/<int:trend_id>', methods=['PUT'])
def update_trend(trend_id):
    data = request.json
    query = f'''
        UPDATE trends
        SET skill_alignments = '{data['skill_alignments']}', career_alignments = '{data['career_alignments']}'
        WHERE position_id = {trend_id}
    '''
    cursor = db.get_db().cursor()
    current_app.logger.info(f'Query: {query}')
    try:
        cursor.execute(query)
        db.get_db().commit()
        response = make_response(jsonify({"message": "Trend updated successfully"}), 200)
    except Exception as e:
        current_app.logger.error(f"Error updating trend: {str(e)}")
        response = make_response(jsonify({"error": "Failed to update trend"}), 500)
    return response

# Route to delete a trend (Jennifer's 4th Story)
@jennifer.route('/trends/<int:trend_id>', methods=['DELETE'])
def delete_trend(trend_id):
    query = f"DELETE FROM trends WHERE position_id = {trend_id}"
    cursor = db.get_db().cursor()
    current_app.logger.info(f'Query: {query}')
    try:
        cursor.execute(query)
        db.get_db().commit()
        response = make_response(jsonify({"message": "Trend deleted successfully"}), 200)
    except Exception as e:
        current_app.logger.error(f"Error deleting trend: {str(e)}")
        response = make_response(jsonify({"error": "Failed to delete trend"}), 500)
    return response

# Route to fetch reports assigned to data analysts (Jennifer's 5th Story)
@jennifer.route('/reports', methods=['GET'])
def get_reports():
    query = '''
        SELECT r.report_name, r.industry_compare, r.timestamp, d.name AS created_by
        FROM reports r
        JOIN data_analyst d ON r.created_by = d.id
    '''
    cursor = db.get_db().cursor()
    current_app.logger.info(f'Query: {query}')
    try:
        cursor.execute(query)
        reports = cursor.fetchall()
        if not reports:
            response = make_response(jsonify({"message": "No reports found"}), 404)
            return response
        response = make_response(jsonify(reports))
        response.status_code = 200
    except Exception as e:
        current_app.logger.error(f"Error fetching reports: {str(e)}")
        response = make_response(jsonify({"error": "Failed to fetch reports"}), 500)
    return response
