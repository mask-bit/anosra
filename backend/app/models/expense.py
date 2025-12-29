from app import db
from datetime import datetime

class Expense(db.Model):
    __tablename__ = 'expenses'
    
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    payment_method = db.Column(db.String(50))
    expense_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text)
    is_recurring = db.Column(db.Boolean, default=False)
    imported_from_open_finance = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'business_id': self.business_id,
            'amount': self.amount,
            'category': self.category,
            'payment_method': self.payment_method,
            'expense_date': self.expense_date.isoformat(),
            'description': self.description,
            'is_recurring': self.is_recurring,
            'imported_from_open_finance': self.imported_from_open_finance,
            'created_at': self.created_at.isoformat()
        }
