from flask import Flask, render_template
from werkzeug.exceptions import HTTPException, InternalServerError

from general.general import general_bp
from projects.projects import projects_bp
from web.makeopensource.projects.loader import ProjectLoader


def create_app():
    app = Flask(__name__)

    app.project_loader = ProjectLoader()
    app.project_loader.load_projects()

    app.register_blueprint(general_bp, url_prefix="/")
    app.register_blueprint(projects_bp, url_prefix="/projects")

    @app.errorhandler(Exception)
    def handle_exception(e):
        if not isinstance(e, HTTPException):
            e = InternalServerError()
        return render_template("general/error.html", error=e), e.code

    return app


def main():
    app = create_app()
    app.run(host="127.0.0.1", port=5877, debug=True)


if __name__ == "__main__":
    main()
