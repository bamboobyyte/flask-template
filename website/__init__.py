from flask import Flask

def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "hello world"

    from .pages import pages
    from .home import home

    # Registering blueprints
    app.register_blueprint(pages, url_pregix='/')
    app.register_blueprint(home, url_pregix='/')
    
    return app