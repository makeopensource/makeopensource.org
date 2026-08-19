# Creating Projects

Project details are written in Markdown files stored in the web/makeopensource/content/projects directory. To create a
new project, create a new Markdown file in that directory with the following front matter at the top:

```yaml
---
name: Project Name
slug: a-short-slug-for-url
description: A short description
github_url: https://github.com/makeopensource/...
archived: True
---
```

The `name`, `slug`, and `description` fields are required. The `github_url` field is optional, but if provided, it will
display a link to the GitHub repository for the project. The `archived` field is also optional; if set to `True`, the
project will be marked as a "Past Project" on the website.

After this header, you can write the content of the project page in Markdown. You can use headings, lists, images, and
other Markdown features to format the content as needed. Do not use an H1 since the project page will already have one.
The project name, description, and GitHub link will be automatically displayed at the top of the page based on the front
matter. You should use H2s and smaller for the rest of the content.