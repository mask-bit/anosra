from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.business_service import BusinessService

business_bp = Blueprint('business', __name__)
business_service = BusinessService()

@business_bp.route('/', methods=['POST'])
@jwt_required()
def create_business():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    result = business_service.create_business(user_id, data)
    
    if result['success']:
        return jsonify(result), 201
    return jsonify(result), 400

@business_bp.route('/', methods=['GET'])
@jwt_required()
def get_businesses():
    user_id = get_jwt_identity()
    result = business_service.get_user_businesses(user_id)
    
    return jsonify(result), 200

@business_bp.route('/<int:business_id>', methods=['GET'])
@jwt_required()
def get_business(business_id):
    user_id = get_jwt_identity()
    result = business_service.get_business(business_id, user_id)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 404

@business_bp.route('/<int:business_id>', methods=['PUT'])
@jwt_required()
def update_business(business_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    
    result = business_service.update_business(business_id, user_id, data)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 400

@business_bp.route('/<int:business_id>', methods=['DELETE'])
@jwt_required()
def delete_business(business_id):
    user_id = get_jwt_identity()
    result = business_service.delete_business(business_id, user_id)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 404
