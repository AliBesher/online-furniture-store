from app.routes.checkout_routes import checkout_bp

app.register_blueprint(checkout_bp, url_prefix="/api")
