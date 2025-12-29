from app import db
from app.models.business import Business
from app.models.expense import Expense
from datetime import datetime, timedelta
import random

class OpenFinanceService:
    """
    Serviço simulado de Open Finance.
    Em produção, deve integrar com APIs reais dos bancos.
    """
    
    def connect_bank(self, user_id, business_id, bank_code):
        business = Business.query.filter_by(id=business_id, user_id=user_id).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        # Simula conexão com banco
        bank_names = {
            '001': 'Banco do Brasil',
            '237': 'Bradesco',
            '341': 'Itaú',
            '033': 'Santander',
            '104': 'Caixa Econômica'
        }
        
        business.open_finance_connected = True
        business.open_finance_bank = bank_names.get(bank_code, 'Banco Desconhecido')
        business.open_finance_last_sync = datetime.utcnow()
        
        try:
            db.session.commit()
            
            # Simula importação inicial de transações
            self._import_sample_transactions(business_id)
            
            return {
                'success': True,
                'message': f'Conectado com sucesso ao {business.open_finance_bank}',
                'bank': business.open_finance_bank
            }
        except Exception as e:
            db.session.rollback()
            return {'success': False, 'message': str(e)}
    
    def disconnect_bank(self, user_id, business_id):
        business = Business.query.filter_by(id=business_id, user_id=user_id).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        business.open_finance_connected = False
        business.open_finance_bank = None
        
        try:
            db.session.commit()
            
            return {
                'success': True,
                'message': 'Conexão com Open Finance removida com sucesso'
            }
        except Exception as e:
            db.session.rollback()
            return {'success': False, 'message': str(e)}
    
    def sync_transactions(self, user_id, business_id):
        business = Business.query.filter_by(id=business_id, user_id=user_id).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        if not business.open_finance_connected:
            return {'success': False, 'message': 'Open Finance não está conectado'}
        
        # Simula sincronização
        imported_count = self._import_sample_transactions(business_id)
        
        business.open_finance_last_sync = datetime.utcnow()
        
        try:
            db.session.commit()
            
            return {
                'success': True,
                'message': f'{imported_count} transações importadas com sucesso',
                'imported_count': imported_count
            }
        except Exception as e:
            db.session.rollback()
            return {'success': False, 'message': str(e)}
    
    def get_connection_status(self, user_id, business_id):
        business = Business.query.filter_by(id=business_id, user_id=user_id).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        return {
            'success': True,
            'status': {
                'connected': business.open_finance_connected,
                'bank': business.open_finance_bank,
                'last_sync': business.open_finance_last_sync.isoformat() if business.open_finance_last_sync else None
            }
        }
    
    def _import_sample_transactions(self, business_id):
        """
        Simula importação de transações.
        Em produção, faria chamadas reais à API Open Finance.
        """
        categories = ['Ingredientes', 'Energia', 'Fornecedores', 'Impostos', 'Manutenção']
        payment_methods = ['Débito', 'Crédito', 'PIX', 'Boleto']
        
        imported_count = 0
        
        for i in range(5):
            expense = Expense(
                business_id=business_id,
                amount=random.uniform(100, 2000),
                category=random.choice(categories),
                payment_method=random.choice(payment_methods),
                expense_date=(datetime.now() - timedelta(days=random.randint(1, 30))).date(),
                description=f'Transação importada via Open Finance',
                imported_from_open_finance=True
            )
            
            db.session.add(expense)
            imported_count += 1
        
        db.session.commit()
        
        return imported_count
