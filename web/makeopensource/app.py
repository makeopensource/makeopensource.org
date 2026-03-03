from flask import Flask

from general.general import general_bp
from projects.projects import projects_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(general_bp, url_prefix="/")
    app.register_blueprint(projects_bp, url_prefix="/projects")

    return app


def main():
    app = create_app()
    app.run(host="127.0.0.1", port=8080, debug=True)


if __name__ == "__main__":
    main()
