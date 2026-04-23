import os.path
from pathlib import Path

import frontmatter
import markdown
from frontmatter import Post
from pydantic import ValidationError

from web.makeopensource.general.paths import get_content_dir
from web.makeopensource.projects.models import ParsedProject, ProjectMetadata


class ProjectLoader:
    def __init__(self):
        self._projects_directory = get_content_dir() / "projects"
        self._projects: dict[str, ParsedProject] = {}  # slug -> project
        self._projects_sorted: list[ParsedProject] = []

    def get_projects(self) -> list[ParsedProject]:
        # Returns a list of all projects for displaying on the projects page
        return self._projects_sorted

    def get_project(self, slug: str) -> ParsedProject | None:
        # Returns the details for a particular project, or None if not found
        return self._projects.get(slug, None)

    @staticmethod
    def parse_project_from_markdown(markdown_file_path: Path) -> ParsedProject:
        assert markdown_file_path.is_file(), f"File not found: {markdown_file_path}"
        with open(markdown_file_path, "r") as f:
            data: Post = frontmatter.load(f)
            try:
                metadata: ProjectMetadata = ProjectMetadata(**data.metadata)
            except ValidationError as e:
                raise ValueError(
                    f"Invalid metadata in project file: {markdown_file_path} {e}"
                )

        html_content: str = markdown.markdown(data.content)
        return ParsedProject(metadata=metadata, body_html=html_content)

    def load_projects(self):
        # Reads Markdown files and stores their parsed content in self._projects
        for markdown_file_path in self._projects_directory.glob("*.md"):
            try:
                project = self.parse_project_from_markdown(markdown_file_path)
                self._projects[project.metadata.slug] = project
                self._projects_sorted.append(project)
            except Exception as e:
                print(f"Error loading project from {markdown_file_path}: {e}")

        self._projects_sorted.sort(
            key=lambda p: p.metadata.name.lower()
        )  # Sort projects alphabetically by name
