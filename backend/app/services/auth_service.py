from app import db
from app.models.user import User
from flask_jwt_extended import create_access_token

class AuthService:
    def register_user(self, email, password, store_name, owner_name):
        if not all([email, password, store_name, owner_name]):
            return {'success': False, 'message': 'Todos os campos são obrigatórios'}
        
        if User.query.filter_by(email=email).first():
            return {'success': False, 'message': 'Email já cadastrado'}
        
        user = User(
            email=email,
            store_name=store_name,
            owner_name=owner_name
        )
        user.set_password(password)
        
        try:
            db.session.add(user)
            db.session.commit()
            
            access_token = create_access_token(identity=user.id)
            
            return {
                'success': True,
                'message': 'Usuário cadastrado com sucesso',
                'user': user.to_dict(),
                'token': access_token
            }
        except Exception as e:
            db.session.rollback()
            return {'success': False, 'message': str(e)}
    
    def login_user(self, email, password):
        if not email or not password:
            return {'success': False, 'message': 'Email e senha são obrigatórios'}
        
        user = User.query.filter_by(email=email).first()
        
        if not user or not user.check_password(password):
            return {'success': False, 'message': 'Email ou senha incorretos'}
        
        access_token = create_access_token(identity=user.id)
        
        return {
            'success': True,
            'message': 'Login realizado com sucesso',
            'user': user.to_dict(),
            'token': access_token
        }
    
    def get_user_by_id(self, user_id):
        user = User.query.get(user_id)
        
        if not user:
            return {'success': False, 'message': 'Usuário não encontrado'}
        
        return {
            'success': True,
            'user': user.to_dict()
        }
    
    def request_password_reset(self, email):
        """Request password reset - sends email with reset link"""
        user = User.query.filter_by(email=email).first()
        
        if not user:
            # For security, don't reveal if email exists
            return {
                'success': True,
                'message': 'Se o e-mail existir, você receberá instruções para redefinir sua senha'
            }
        
        # In production, generate reset token and send email
        # For now, simulate the process
        # TODO: Integrate with email service (SendGrid, AWS SES, etc)
        # TODO: Generate secure reset token with expiration
        
        return {
            'success': True,
            'message': 'Instruções de recuperação enviadas para o e-mail cadastrado'
        }
