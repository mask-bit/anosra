from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.report_service import ReportService

reports_bp = Blueprint('reports', __name__)
report_service = ReportService()

@reports_bp.route('/financial/<int:business_id>', methods=['GET'])
@jwt_required()
def get_financial_report(business_id):
    user_id = get_jwt_identity()
    period = request.args.get('period', 'month')
    
    result = report_service.generate_financial_report(business_id, user_id, period)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 404

@reports_bp.route('/employees/<int:business_id>', methods=['GET'])
@jwt_required()
def get_employee_report(business_id):
    user_id = get_jwt_identity()
    
    result = report_service.generate_employee_report(business_id, user_id)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 404

@reports_bp.route('/business/<int:business_id>', methods=['GET'])
@jwt_required()
def get_business_report(business_id):
    user_id = get_jwt_identity()
    
    result = report_service.generate_business_report(business_id, user_id)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 404

@reports_bp.route('/inconsistencies/<int:business_id>', methods=['GET'])
@jwt_required()
def get_inconsistencies(business_id):
    user_id = get_jwt_identity()
    
    result = report_service.detect_inconsistencies(business_id, user_id)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 404

@reports_bp.route('/comparative/<int:business_id>', methods=['GET'])
@jwt_required()
def get_comparative_report(business_id):
    user_id = get_jwt_identity()
    
    result = report_service.generate_comparative_report(business_id, user_id)
    
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 404
