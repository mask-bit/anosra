from app import db
from datetime import datetime

class Employee(db.Model):
    __tablename__ = 'employees'
    
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    employment_type = db.Column(db.String(50))  # fixo, variavel, diarista
    start_date = db.Column(db.Date, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def calculate_total_cost(self):
        """Calcula custo total incluindo encargos estimados (40%)"""
        return self.salary * 1.4
    
    def to_dict(self):
        return {
            'id': self.id,
            'business_id': self.business_id,
            'name': self.name,
            'role': self.role,
            'salary': self.salary,
            'total_cost': self.calculate_total_cost(),
            'employment_type': self.employment_type,
            'start_date': self.start_date.isoformat(),
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat()
        }
