from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    result = auth_service.register_user(
        email=data.get('email'),
        password=data.get('password'),
        store_name=data.get('store_name'),
        owner_name=data.get('owner_name')
    )
    
    if result['success']:
        return jsonify(result), 201
    return jsonify(result), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    result = auth_service.login_user(
        email=data.get('email'),
        password=data.get('password')
    )
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 401

@auth_bp.route('/recover-password', methods=['POST'])
def recover_password():
    """Send password recovery email"""
    data = request.get_json()
    email = data.get('email')
    
    if not email:
        return jsonify({
            'success': False,
            'message': 'E-mail é obrigatório'
        }), 400
    
    # For now, simulate email sending
    # In production, integrate with email service
    result = auth_service.request_password_reset(email)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 404

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    user_id = get_jwt_identity()
    result = auth_service.get_user_by_id(user_id)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 404
