from app import db
from datetime import datetime

class Business(db.Model):
    __tablename__ = 'businesses'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    business_type = db.Column(db.String(100), nullable=False)
    employee_count = db.Column(db.Integer, default=0)
    has_different_roles = db.Column(db.Boolean, default=False)
    monthly_revenue = db.Column(db.Float, default=0)
    monthly_expenses = db.Column(db.Float, default=0)
    main_revenue_source = db.Column(db.String(200))
    main_expense_type = db.Column(db.String(200))
    start_date = db.Column(db.Date)
    open_finance_connected = db.Column(db.Boolean, default=False)
    open_finance_bank = db.Column(db.String(100))
    open_finance_last_sync = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamentos
    expenses = db.relationship('Expense', backref='business', lazy=True, cascade='all, delete-orphan')
    employees = db.relationship('Employee', backref='business', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'business_type': self.business_type,
            'employee_count': self.employee_count,
            'has_different_roles': self.has_different_roles,
            'monthly_revenue': self.monthly_revenue,
            'monthly_expenses': self.monthly_expenses,
            'main_revenue_source': self.main_revenue_source,
            'main_expense_type': self.main_expense_type,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'open_finance_connected': self.open_finance_connected,
            'open_finance_bank': self.open_finance_bank,
            'open_finance_last_sync': self.open_finance_last_sync.isoformat() if self.open_finance_last_sync else None,
            'created_at': self.created_at.isoformat()
        }
