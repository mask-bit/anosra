from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.expense_service import ExpenseService

expense_bp = Blueprint('expense', __name__)
expense_service = ExpenseService()

@expense_bp.route('/', methods=['POST'])
@jwt_required()
def create_expense():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    result = expense_service.create_expense(user_id, data)
    
    if result['success']:
        return jsonify(result), 201
    return jsonify(result), 400

@expense_bp.route('/business/<int:business_id>', methods=['GET'])
@jwt_required()
def get_expenses(business_id):
    user_id = get_jwt_identity()
    period = request.args.get('period', 'month')
    
    result = expense_service.get_expenses(business_id, user_id, period)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 404

@expense_bp.route('/<int:expense_id>', methods=['PUT'])
@jwt_required()
def update_expense(expense_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    
    result = expense_service.update_expense(expense_id, user_id, data)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 400

@expense_bp.route('/<int:expense_id>', methods=['DELETE'])
@jwt_required()
def delete_expense(expense_id):
    user_id = get_jwt_identity()
    result = expense_service.delete_expense(expense_id, user_id)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 404

@expense_bp.route('/business/<int:business_id>/summary', methods=['GET'])
@jwt_required()
def get_expense_summary(business_id):
    user_id = get_jwt_identity()
    result = expense_service.get_expense_summary(business_id, user_id)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 404
