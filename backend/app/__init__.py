from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
from app.config import Config
import os

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    root_dir = os.path.abspath(os.path.join(base_dir, '../..'))
    template_dir = os.path.join(root_dir, 'frontend/templates')
    static_dir = os.path.join(root_dir, 'frontend/static')
    
    app = Flask(__name__, 
                template_folder=template_dir,
                static_folder=static_dir,
                static_url_path='/static')
    app.config.from_object(Config)
    
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)
    migrate.init_app(app, db)
    
    @app.route('/debug')
    def debug_info():
        templates_exist = os.path.exists(app.template_folder)
        templates_list = []
        if templates_exist:
            templates_list = [f for f in os.listdir(app.template_folder) if f.endswith('.html')]
        
        return {
            'status': 'OK',
            'template_folder': app.template_folder,
            'static_folder': app.static_folder,
            'templates_exist': templates_exist,
            'static_exist': os.path.exists(app.static_folder),
            'templates_count': len(templates_list),
            'templates_list': sorted(templates_list)
        }
    
    from app.routes.auth import auth_bp
    from app.routes.business import business_bp
    from app.routes.expense import expense_bp
    from app.routes.employee import employee_bp
    from app.routes.reports import reports_bp
    from app.routes.integration import integration_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(business_bp, url_prefix='/api/business')
    app.register_blueprint(expense_bp, url_prefix='/api/expenses')
    app.register_blueprint(employee_bp, url_prefix='/api/employees')
    app.register_blueprint(reports_bp, url_prefix='/api/reports')
    app.register_blueprint(integration_bp, url_prefix='/api/integration')
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/login')
    def login():
        return render_template('login.html')
    
    @app.route('/cadastro')
    def cadastro():
        return render_template('cadastro.html')
    
    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html')
    
    @app.route('/negocios')
    def negocios():
        return render_template('negocios.html')
    
    @app.route('/despesas')
    def despesas():
        return render_template('despesas.html')
    
    @app.route('/funcionarios')
    def funcionarios():
        return render_template('funcionarios.html')
    
    @app.route('/relatorios')
    def relatorios():
        return render_template('relatorios.html')
    
    @app.route('/integracao')
    def integracao():
        return render_template('integracao.html')
    
    @app.route('/configuracoes')
    def configuracoes():
        return render_template('configuracoes.html')
    
    @app.route('/recuperar-senha')
    def recuperar_senha():
        return render_template('recuperar-senha.html')
    
    return app
