from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            print("\n" + "="*60)
            print("✓ Banco de dados inicializado com sucesso!")
            print("="*60)
            print("\n🚀 Servidor Anosra iniciando...")
            print("\n📍 Acesse o sistema em: http://localhost:5000")
            print("\n📄 Páginas disponíveis:")
            print("   • http://localhost:5000/         (Landing Page)")
            print("   • http://localhost:5000/login    (Login)")
            print("   • http://localhost:5000/cadastro (Cadastro)")
            print("   • http://localhost:5000/dashboard (Dashboard)")
            print("\n🔧 Debug info: http://localhost:5000/debug")
            print("\n" + "="*60 + "\n")
        except Exception as e:
            print(f"\n❌ Erro ao inicializar banco de dados: {e}")
            print("Verifique o arquivo .env e as configurações.\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
