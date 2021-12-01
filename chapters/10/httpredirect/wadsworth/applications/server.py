from sanic import Sanic
from wadsworth.blueprints.view import bp
from wadsworth.blueprints.info.view import bp as info_view
from wadsworth.applications.redirect import attach_redirect_app


def create_app():
    app = Sanic("MainApp")
    app.config.SERVER_NAME = "localhost:8443"
    app.blueprint(bp)
    app.blueprint(info_view)

    attach_redirect_app(app)

    return app
