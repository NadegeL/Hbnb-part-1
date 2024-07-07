# src/routes/routes.py

def register_routes(app):
    from .users import users_bp
    from .countries import countries_bp
    # Register more blueprints as necessary
    app.register_blueprint(users_bp)
    app.register_blueprint(countries_bp)
