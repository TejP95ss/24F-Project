from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

gavin = Blueprint('gavin', __name__)