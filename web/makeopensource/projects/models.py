import string

from pydantic import BaseModel, field_validator


class ProjectMetadata(BaseModel):
    name: str
    slug: str
    description: str | None = None
    github_url: str | None = None

    @field_validator("slug")
    @classmethod
    def slug_validator(cls, v: str):
        allowed_chars = string.ascii_lowercase + string.digits + "-"
        if not all(c in allowed_chars for c in v):
            raise ValueError(
                "Slug can only contain lowercase letters, digits, and hyphens."
            )
        return v


class ParsedProject(BaseModel):
    metadata: ProjectMetadata
    body_html: str
