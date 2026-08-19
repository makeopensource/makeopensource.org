from flask import Blueprint, render_template, current_app, abort

from web.makeopensource.projects.models import ParsedProject, GroupedProjects

projects_bp = Blueprint("projects", __name__)


@projects_bp.get("/")
def index():
    projects: GroupedProjects = current_app.project_loader.get_projects()
    return render_template("projects/projects_index.html", projects=projects)


@projects_bp.get("/<project_slug>")
def project(project_slug: str):
    proj: ParsedProject | None = current_app.project_loader.get_project(
        project_slug.lower()
    )
    if not proj:
        abort(404, description=f'Project "{project_slug}" doesn\'t exist.')
    return render_template("projects/project.html", project=proj)
