from app import db
from app.models.business import Business
from app.models.user import User

class BusinessService:
    def create_business(self, user_id, data):
        user = User.query.get(user_id)
        if not user:
            return {'success': False, 'message': 'Usuário não encontrado'}
        
        business = Business(
            user_id=user_id,
            business_type=data.get('business_type'),
            employee_count=data.get('employee_count', 0),
            has_different_roles=data.get('has_different_roles', False),
            monthly_revenue=data.get('monthly_revenue', 0),
            monthly_expenses=data.get('monthly_expenses', 0),
            main_revenue_source=data.get('main_revenue_source'),
            main_expense_type=data.get('main_expense_type')
        )
        
        try:
            db.session.add(business)
            db.session.commit()
            
            return {
                'success': True,
                'message': 'Negócio criado com sucesso',
                'business': business.to_dict()
            }
        except Exception as e:
            db.session.rollback()
            return {'success': False, 'message': str(e)}
    
    def get_user_businesses(self, user_id):
        businesses = Business.query.filter_by(user_id=user_id).all()
        
        return {
            'success': True,
            'businesses': [b.to_dict() for b in businesses]
        }
    
    def get_business(self, business_id, user_id):
        business = Business.query.filter_by(id=business_id, user_id=user_id).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        return {
            'success': True,
            'business': business.to_dict()
        }
    
    def update_business(self, business_id, user_id, data):
        business = Business.query.filter_by(id=business_id, user_id=user_id).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        for key, value in data.items():
            if hasattr(business, key):
                setattr(business, key, value)
        
        try:
            db.session.commit()
            
            return {
                'success': True,
                'message': 'Negócio atualizado com sucesso',
                'business': business.to_dict()
            }
        except Exception as e:
            db.session.rollback()
            return {'success': False, 'message': str(e)}
    
    def delete_business(self, business_id, user_id):
        business = Business.query.filter_by(id=business_id, user_id=user_id).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        try:
            db.session.delete(business)
            db.session.commit()
            
            return {
                'success': True,
                'message': 'Negócio excluído com sucesso'
            }
        except Exception as e:
            db.session.rollback()
            return {'success': False, 'message': str(e)}
