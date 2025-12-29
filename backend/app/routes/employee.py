from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.expense_service import ExpenseService

employee_bp = Blueprint('employee', __name__)
expense_service = ExpenseService()

@employee_bp.route('/', methods=['POST'])
@jwt_required()
def create_employee():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    result = expense_service.create_employee(user_id, data)
    
    if result['success']:
        return jsonify(result), 201
    return jsonify(result), 400

@employee_bp.route('/business/<int:business_id>', methods=['GET'])
@jwt_required()
def get_employees(business_id):
    user_id = get_jwt_identity()
    result = expense_service.get_employees(business_id, user_id)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 404

@employee_bp.route('/<int:employee_id>', methods=['PUT'])
@jwt_required()
def update_employee(employee_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    
    result = expense_service.update_employee(employee_id, user_id, data)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 400

@employee_bp.route('/<int:employee_id>', methods=['DELETE'])
@jwt_required()
def delete_employee(employee_id):
    user_id = get_jwt_identity()
    result = expense_service.delete_employee(employee_id, user_id)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 404

@employee_bp.route('/business/<int:business_id>/analysis', methods=['GET'])
@jwt_required()
def get_employee_analysis(business_id):
    user_id = get_jwt_identity()
    result = expense_service.get_employee_analysis(business_id, user_id)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 404
