from pathlib import Path

# Don't move this file; it uses its relative path to determine the path of everything else.


def get_makeopensource_dir() -> Path:
    return Path(__file__).resolve().parent.parent


def get_content_dir() -> Path:
    return get_makeopensource_dir() / "content"
