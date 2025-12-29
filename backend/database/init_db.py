"""
Script para inicializar o banco de dados
"""
from app import create_app, db
from app.models import User, Business, Employee, Expense, OpenFinanceConnection

def init_database():
    """Criar todas as tabelas do banco de dados"""
    app = create_app()
    
    with app.app_context():
        # Criar todas as tabelas
        db.create_all()
        print("✓ Banco de dados inicializado com sucesso!")
        print("✓ Todas as tabelas foram criadas")

if __name__ == "__main__":
    init_database()
