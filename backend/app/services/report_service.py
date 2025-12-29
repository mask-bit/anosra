from app.models.business import Business
from app.models.expense import Expense
from app.models.employee import Employee
from datetime import datetime, timedelta
from sqlalchemy import func
from app import db

class ReportService:
    def generate_financial_report(self, business_id, user_id, period='month'):
        business = Business.query.filter_by(id=business_id, user_id=user_id).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        date_filter = self._get_date_filter(period)
        
        expenses = db.session.query(func.sum(Expense.amount)).filter(
            Expense.business_id == business_id,
            Expense.expense_date >= date_filter
        ).scalar() or 0
        
        revenue = business.monthly_revenue
        profit = revenue - expenses
        profit_margin = (profit / revenue * 100) if revenue > 0 else 0
        
        last_period_filter = date_filter - timedelta(days=30)
        last_expenses = db.session.query(func.sum(Expense.amount)).filter(
            Expense.business_id == business_id,
            Expense.expense_date >= last_period_filter,
            Expense.expense_date < date_filter
        ).scalar() or 0
        
        change_percent = 0
        if last_expenses > 0:
            change_percent = ((expenses - last_expenses) / last_expenses) * 100
        
        analysis = self._generate_financial_analysis(profit, profit_margin, change_percent)
        
        return {
            'success': True,
            'report': {
                'revenue': revenue,
                'expenses': expenses,
                'profit': profit,
                'profit_margin': round(profit_margin, 2),
                'change_percent': round(change_percent, 2),
                'analysis': analysis
            }
        }
    
    def generate_employee_report(self, business_id, user_id):
        business = Business.query.filter_by(id=business_id, user_id=user_id).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        employees = Employee.query.filter_by(business_id=business_id, is_active=True).all()
        
        total_cost = sum(e.calculate_total_cost() for e in employees)
        payroll_percentage = (total_cost / business.monthly_revenue * 100) if business.monthly_revenue > 0 else 0
        
        industry_average = self._get_industry_average_payroll(business.business_type)
        
        analysis = self._generate_employee_analysis(payroll_percentage, industry_average, business.business_type)
        
        return {
            'success': True,
            'report': {
                'total_employees': len(employees),
                'total_cost': total_cost,
                'payroll_percentage': round(payroll_percentage, 2),
                'industry_average': industry_average,
                'analysis': analysis
            }
        }
    
    def generate_business_report(self, business_id, user_id):
        business = Business.query.filter_by(id=business_id, user_id=user_id).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        revenue = business.monthly_revenue
        expenses = business.monthly_expenses
        profit_margin = ((revenue - expenses) / revenue * 100) if revenue > 0 else 0
        
        industry_margin = self._get_industry_average_margin(business.business_type)
        
        analysis = self._generate_business_analysis(profit_margin, industry_margin, business.business_type)
        
        return {
            'success': True,
            'report': {
                'business_type': business.business_type,
                'profit_margin': round(profit_margin, 2),
                'industry_average_margin': industry_margin,
                'performance': 'acima da média' if profit_margin > industry_margin else 'abaixo da média',
                'analysis': analysis
            }
        }
    
    def detect_inconsistencies(self, business_id, user_id):
        business = Business.query.filter_by(id=business_id, user_id=user_id).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        inconsistencies = []
        
        # Verifica receita vs funcionários
        employees_count = Employee.query.filter_by(business_id=business_id, is_active=True).count()
        if employees_count > 0:
            revenue_per_employee = business.monthly_revenue / employees_count
            if revenue_per_employee < 3000:
                inconsistencies.append({
                    'type': 'warning',
                    'title': 'Receita baixa por funcionário',
                    'message': f'Sua receita por funcionário é de R$ {revenue_per_employee:.2f}. Isso pode indicar baixa produtividade ou receita subdeclarada.'
                })
        
        # Verifica margem negativa
        profit = business.monthly_revenue - business.monthly_expenses
        if profit < 0:
            inconsistencies.append({
                'type': 'alert',
                'title': 'Margem negativa',
                'message': 'Seus gastos são maiores que sua receita. É importante revisar despesas ou aumentar faturamento.'
            })
        
        # Verifica gastos crescentes
        current_month = datetime.now().replace(day=1).date()
        last_month = (datetime.now().replace(day=1) - timedelta(days=1)).replace(day=1).date()
        
        current_expenses = db.session.query(func.sum(Expense.amount)).filter(
            Expense.business_id == business_id,
            Expense.expense_date >= current_month
        ).scalar() or 0
        
        last_month_expenses = db.session.query(func.sum(Expense.amount)).filter(
            Expense.business_id == business_id,
            Expense.expense_date >= last_month,
            Expense.expense_date < current_month
        ).scalar() or 0
        
        if last_month_expenses > 0 and current_expenses > last_month_expenses * 1.2:
            increase = ((current_expenses - last_month_expenses) / last_month_expenses) * 100
            inconsistencies.append({
                'type': 'warning',
                'title': 'Aumento significativo de gastos',
                'message': f'Seus gastos cresceram {increase:.1f}% em relação ao mês anterior, mas a receita se manteve estável.'
            })
        
        return {
            'success': True,
            'inconsistencies': inconsistencies
        }
    
    def generate_comparative_report(self, business_id, user_id):
        business = Business.query.filter_by(id=business_id, user_id=user_id).first()
        
        if not business:
            return {'success': False, 'message': 'Negócio não encontrado'}
        
        # Comparação histórica (últimos 3 meses)
        months_data = []
        for i in range(3):
            month_start = (datetime.now().replace(day=1) - timedelta(days=30 * i)).date()
            month_end = month_start + timedelta(days=30)
            
            month_expenses = db.session.query(func.sum(Expense.amount)).filter(
                Expense.business_id == business_id,
                Expense.expense_date >= month_start,
                Expense.expense_date < month_end
            ).scalar() or 0
            
            months_data.append({
                'month': month_start.strftime('%B'),
                'expenses': month_expenses,
                'revenue': business.monthly_revenue,
                'profit': business.monthly_revenue - month_expenses
            })
        
        # Calcula evolução
        if len(months_data) >= 2:
            recent_profit = months_data[0]['profit']
            old_profit = months_data[-1]['profit']
            evolution = ((recent_profit - old_profit) / abs(old_profit) * 100) if old_profit != 0 else 0
        else:
            evolution = 0
        
        return {
            'success': True,
            'report': {
                'historical_data': months_data,
                'evolution_percent': round(evolution, 2),
                'analysis': f'Você {"evoluiu" if evolution > 0 else "regrediu"} {abs(evolution):.1f}% nos últimos 3 meses.'
            }
        }
    
    # Helper methods
    def _get_date_filter(self, period):
        now = datetime.now().date()
        if period == 'month':
            return now - timedelta(days=30)
        elif period == '3months':
            return now - timedelta(days=90)
        elif period == '6months':
            return now - timedelta(days=180)
        return now - timedelta(days=30)
    
    def _get_industry_average_payroll(self, business_type):
        averages = {
            'Restaurante': 35,
            'Lanchonete': 30,
            'Hotel': 40,
            'Loja física': 25,
            'Loja online': 20,
            'Prestador de serviços': 30,
            'Igreja': 15,
            'Escola': 60,
            'Clínica': 45,
            'Autônomo': 10
        }
        return averages.get(business_type, 30)
    
    def _get_industry_average_margin(self, business_type):
        margins = {
            'Restaurante': 18,
            'Lanchonete': 15,
            'Hotel': 25,
            'Loja física': 20,
            'Loja online': 30,
            'Prestador de serviços': 35,
            'Igreja': 10,
            'Escola': 20,
            'Clínica': 30,
            'Autônomo': 40
        }
        return margins.get(business_type, 20)
    
    def _generate_financial_analysis(self, profit, margin, change):
        if profit < 0:
            return "Seu negócio está operando com prejuízo. É urgente revisar despesas e buscar aumento de receita."
        elif margin < 10:
            return f"Sua margem de lucro de {margin:.1f}% está baixa. Considere reduzir custos ou ajustar preços."
        elif change < -10:
            return f"Seu lucro caiu {abs(change):.1f}% em relação ao período anterior. Atenção aos custos."
        elif change > 10:
            return f"Excelente! Seu lucro aumentou {change:.1f}% em relação ao período anterior."
        else:
            return "Seu negócio está estável. Continue monitorando os indicadores."
    
    def _generate_employee_analysis(self, payroll_pct, industry_avg, business_type):
        if payroll_pct > industry_avg + 10:
            return f"Gastos com funcionários acima da média para {business_type}. Média do setor: {industry_avg}%."
        elif payroll_pct < industry_avg - 10:
            return f"Gastos com funcionários abaixo da média. Você pode estar subutilizando a equipe."
        else:
            return f"Gastos com funcionários dentro da média esperada para {business_type}."
    
    def _generate_business_analysis(self, margin, industry_margin, business_type):
        if margin > industry_margin:
            diff = margin - industry_margin
            return f"Parabéns! Sua margem está {diff:.1f}% acima da média de {business_type}."
        else:
            diff = industry_margin - margin
            return f"Negócios como o seu costumam ter margem de {industry_margin}%. O seu está {diff:.1f}% abaixo. Considere otimizar custos."
