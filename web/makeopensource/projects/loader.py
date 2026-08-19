from pathlib import Path

import frontmatter
import markdown
from frontmatter import Post
from pydantic import ValidationError

from web.makeopensource.general.paths import get_content_dir
from web.makeopensource.projects.models import (
    ParsedProject,
    ProjectMetadata,
    GroupedProjects,
)


class ProjectLoader:
    def __init__(self):
        self._projects_directory = get_content_dir() / "projects"
        self._projects: dict[str, ParsedProject] = {}  # slug -> project
        self._grouped_projects: GroupedProjects = GroupedProjects()

    def get_projects(self) -> GroupedProjects:
        # Returns projects grouped by section (current/past) for displaying on the projects page
        return self._grouped_projects

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
        # Reads Markdown files and stores their parsed content in self._projects and self._grouped_projects
        for markdown_file_path in self._projects_directory.glob("*.md"):
            try:
                project = self.parse_project_from_markdown(markdown_file_path)

                if project.metadata.slug in self._projects:
                    raise ValueError(f'Duplicate slug "{project.metadata.slug}" found')

                self._projects[project.metadata.slug] = project

                if project.metadata.archived:
                    self._grouped_projects.past.append(project)
                else:
                    self._grouped_projects.current.append(project)
            except Exception as e:
                print(f"Error loading project from {markdown_file_path}: {e}")

        # Sort projects alphabetically by name within each group
        groups = [self._grouped_projects.past, self._grouped_projects.current]
        for group in groups:
            group.sort(key=lambda p: p.metadata.name.lower())
