"""
Script para popular o banco com dados de exemplo
"""
from app import create_app, db
from app.models import User, Business, Employee, Expense
from datetime import datetime, timedelta
import random

def seed_database():
    """Popular banco com dados de exemplo"""
    app = create_app()
    
    with app.app_context():
        # Limpar dados existentes
        db.drop_all()
        db.create_all()
        
        # Criar usuário de exemplo
        user = User(
            email="demo@anosra.com",
            store_name="Restaurante Demo",
            owner_name="João Silva",
            first_login=False
        )
        user.set_password("demo123456")
        db.session.add(user)
        db.session.commit()
        
        # Criar negócio de exemplo
        business = Business(
            user_id=user.id,
            name="Restaurante Demo",
            business_type="Restaurante",
            category="Alimentação",
            employee_count=5,
            monthly_revenue=50000.0,
            monthly_expenses=35000.0,
            main_revenue_source="Vendas no local",
            main_expense_type="Ingredientes",
            start_date=datetime.now() - timedelta(days=365)
        )
        db.session.add(business)
        db.session.commit()
        
        # Criar funcionários de exemplo
        employees_data = [
            {"name": "Maria Santos", "role": "Gerente", "salary": 4500.0, "type": "fixo"},
            {"name": "Pedro Costa", "role": "Cozinheiro", "salary": 3200.0, "type": "fixo"},
            {"name": "Ana Lima", "role": "Atendente", "salary": 2100.0, "type": "fixo"},
            {"name": "Carlos Souza", "role": "Cozinheiro", "salary": 3000.0, "type": "fixo"},
            {"name": "Juliana Dias", "role": "Atendente", "salary": 2100.0, "type": "fixo"},
        ]
        
        for emp_data in employees_data:
            employee = Employee(
                business_id=business.id,
                name=emp_data["name"],
                role=emp_data["role"],
                salary=emp_data["salary"],
                employment_type=emp_data["type"],
                start_date=datetime.now() - timedelta(days=random.randint(30, 300))
            )
            db.session.add(employee)
        
        # Criar despesas de exemplo
        categories = ["Ingredientes", "Energia", "Gás", "Funcionários", "Aluguel", "Impostos"]
        
        for i in range(30):
            expense = Expense(
                business_id=business.id,
                amount=random.uniform(500, 5000),
                category=random.choice(categories),
                date=datetime.now() - timedelta(days=random.randint(0, 90)),
                payment_method=random.choice(["Dinheiro", "Cartão", "PIX", "Boleto"]),
                description=f"Despesa de {random.choice(categories).lower()}"
            )
            db.session.add(expense)
        
        db.session.commit()
        
        print("✓ Banco de dados populado com sucesso!")
        print(f"✓ Usuário: demo@anosra.com | Senha: demo123456")
        print(f"✓ Negócio: {business.name}")
        print(f"✓ Funcionários: {len(employees_data)}")
        print(f"✓ Despesas: 30 registros")

if __name__ == "__main__":
    seed_database()
