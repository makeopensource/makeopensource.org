from flask import Blueprint, render_template

projects_bp = Blueprint("projects", __name__)


@projects_bp.get("/")
def index():
    return render_template("projects/projects_index.html")


@projects_bp.get("/<project_name>")
def project(project_name: str):
    return render_template("projects/project.html", project_name=project_name)
