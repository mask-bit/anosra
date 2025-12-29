from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.open_finance_service import OpenFinanceService

integration_bp = Blueprint('integration', __name__)
open_finance_service = OpenFinanceService()

@integration_bp.route('/open-finance/connect', methods=['POST'])
@jwt_required()
def connect_open_finance():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    result = open_finance_service.connect_bank(
        user_id=user_id,
        business_id=data.get('business_id'),
        bank_code=data.get('bank_code')
    )
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 400

@integration_bp.route('/open-finance/disconnect/<int:business_id>', methods=['POST'])
@jwt_required()
def disconnect_open_finance(business_id):
    user_id = get_jwt_identity()
    
    result = open_finance_service.disconnect_bank(user_id, business_id)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 400

@integration_bp.route('/open-finance/sync/<int:business_id>', methods=['POST'])
@jwt_required()
def sync_open_finance(business_id):
    user_id = get_jwt_identity()
    
    result = open_finance_service.sync_transactions(user_id, business_id)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 400

@integration_bp.route('/open-finance/status/<int:business_id>', methods=['GET'])
@jwt_required()
def get_open_finance_status(business_id):
    user_id = get_jwt_identity()
    
    result = open_finance_service.get_connection_status(user_id, business_id)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 404
