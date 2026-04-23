from flask import Blueprint, render_template, current_app, abort

from web.makeopensource.projects.models import ParsedProject

projects_bp = Blueprint("projects", __name__)


@projects_bp.get("/")
def index():
    projects: list[ParsedProject] = current_app.project_loader.get_projects()
    return render_template("projects/projects_index.html", projects=projects)


@projects_bp.get("/<project_slug>")
def project(project_slug: str):
    proj: ParsedProject | None = current_app.project_loader.get_project(project_slug)
    if not proj:
        abort(404, description=f"Project not found: {project_slug}")
    return render_template("projects/project.html", project=proj)
