from app import db
from app.models.expense import Expense
from app.models.employee import Employee
from app.models.business import Business
from datetime import datetime, timedelta
from sqlalchemy import func

class ExpenseService:
    def create_expense(self, user_id, data):
        business = Business.query.filter_by(
            id=data.get('business_id'),
            user_id=user_id
        ).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        expense = Expense(
            business_id=data.get('business_id'),
            amount=data.get('amount'),
            category=data.get('category'),
            payment_method=data.get('payment_method'),
            expense_date=datetime.strptime(data.get('expense_date'), '%Y-%m-%d').date(),
            description=data.get('description')
        )
        
        try:
            db.session.add(expense)
            db.session.commit()
            
            return {
                'success': True,
                'message': 'Despesa registrada com sucesso',
                'expense': expense.to_dict()
            }
        except Exception as e:
            db.session.rollback()
            return {'success': False, 'message': str(e)}
    
    def get_expenses(self, business_id, user_id, period='month'):
        business = Business.query.filter_by(id=business_id, user_id=user_id).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        date_filter = datetime.now().date()
        if period == 'month':
            date_filter = date_filter - timedelta(days=30)
        elif period == '3months':
            date_filter = date_filter - timedelta(days=90)
        elif period == '6months':
            date_filter = date_filter - timedelta(days=180)
        
        expenses = Expense.query.filter(
            Expense.business_id == business_id,
            Expense.expense_date >= date_filter
        ).order_by(Expense.expense_date.desc()).all()
        
        return {
            'success': True,
            'expenses': [e.to_dict() for e in expenses]
        }
    
    def get_expense_summary(self, business_id, user_id):
        business = Business.query.filter_by(id=business_id, user_id=user_id).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        current_month = datetime.now().replace(day=1).date()
        last_month = (datetime.now().replace(day=1) - timedelta(days=1)).replace(day=1).date()
        
        current_total = db.session.query(func.sum(Expense.amount)).filter(
            Expense.business_id == business_id,
            Expense.expense_date >= current_month
        ).scalar() or 0
        
        last_month_total = db.session.query(func.sum(Expense.amount)).filter(
            Expense.business_id == business_id,
            Expense.expense_date >= last_month,
            Expense.expense_date < current_month
        ).scalar() or 0
        
        category_breakdown = db.session.query(
            Expense.category,
            func.sum(Expense.amount)
        ).filter(
            Expense.business_id == business_id,
            Expense.expense_date >= current_month
        ).group_by(Expense.category).all()
        
        top_category = max(category_breakdown, key=lambda x: x[1]) if category_breakdown else None
        
        change_percent = 0
        if last_month_total > 0:
            change_percent = ((current_total - last_month_total) / last_month_total) * 100
        
        return {
            'success': True,
            'summary': {
                'total_current_month': current_total,
                'total_last_month': last_month_total,
                'change_percent': round(change_percent, 2),
                'top_category': top_category[0] if top_category else None,
                'top_category_amount': top_category[1] if top_category else 0,
                'category_breakdown': {cat: float(amount) for cat, amount in category_breakdown}
            }
        }
    
    # Employee methods
    def create_employee(self, user_id, data):
        business = Business.query.filter_by(
            id=data.get('business_id'),
            user_id=user_id
        ).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        employee = Employee(
            business_id=data.get('business_id'),
            name=data.get('name'),
            role=data.get('role'),
            salary=data.get('salary'),
            employment_type=data.get('employment_type'),
            start_date=datetime.strptime(data.get('start_date'), '%Y-%m-%d').date()
        )
        
        try:
            db.session.add(employee)
            db.session.commit()
            
            return {
                'success': True,
                'message': 'Funcionário cadastrado com sucesso',
                'employee': employee.to_dict()
            }
        except Exception as e:
            db.session.rollback()
            return {'success': False, 'message': str(e)}
    
    def get_employees(self, business_id, user_id):
        business = Business.query.filter_by(id=business_id, user_id=user_id).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        employees = Employee.query.filter_by(business_id=business_id).all()
        
        return {
            'success': True,
            'employees': [e.to_dict() for e in employees]
        }
    
    def get_employee_analysis(self, business_id, user_id):
        business = Business.query.filter_by(id=business_id, user_id=user_id).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        employees = Employee.query.filter_by(business_id=business_id, is_active=True).all()
        
        total_salary = sum(e.salary for e in employees)
        total_cost = sum(e.calculate_total_cost() for e in employees)
        
        payroll_percentage = 0
        if business.monthly_revenue > 0:
            payroll_percentage = (total_cost / business.monthly_revenue) * 100
        
        industry_average = 35  # Média de mercado estimada
        
        alerts = []
        if payroll_percentage > industry_average:
            alerts.append({
                'type': 'warning',
                'message': f'Folha de pagamento acima da média para {business.business_type}'
            })
        
        return {
            'success': True,
            'analysis': {
                'total_employees': len(employees),
                'total_salary': total_salary,
                'total_cost_with_charges': total_cost,
                'payroll_percentage': round(payroll_percentage, 2),
                'industry_average': industry_average,
                'alerts': alerts
            }
        }
    
    def update_employee(self, employee_id, user_id, data):
        employee = Employee.query.join(Business).filter(
            Employee.id == employee_id,
            Business.user_id == user_id
        ).first()
        
        if not employee:
            return {'success': False, 'message': 'Funcionário não encontrado'}
        
        for key, value in data.items():
            if hasattr(employee, key):
                setattr(employee, key, value)
        
        try:
            db.session.commit()
            
            return {
                'success': True,
                'message': 'Funcionário atualizado com sucesso',
                'employee': employee.to_dict()
            }
        except Exception as e:
            db.session.rollback()
            return {'success': False, 'message': str(e)}
    
    def delete_employee(self, employee_id, user_id):
        employee = Employee.query.join(Business).filter(
            Employee.id == employee_id,
            Business.user_id == user_id
        ).first()
        
        if not employee:
            return {'success': False, 'message': 'Funcionário não encontrado'}
        
        try:
            db.session.delete(employee)
            db.session.commit()
            
            return {
                'success': True,
                'message': 'Funcionário removido com sucesso'
            }
        except Exception as e:
            db.session.rollback()
            return {'success': False, 'message': str(e)}
