
from flask import Flask

def create_app(config=None):
    app = Flask(__name__, template_folder='assets/html', static_folder='assets')

    from .views import graph
    app.register_blueprint(graph.bp)

    return app

