# MakeOpenSource.org

## :warning: Security Reminders
1. In the root directory of the repo, run `python3 generate_key.py` to generate a random individual key.

2. Set DEBUG = True in `mos/settings.py`

3. (mac) Set a global .env file to prevent pushes with `.DS_Store files`


## :file_folder: Directory Structure
There are two applications (directories) currently
- main: static pages and github api integration in the future
- idealab: a hub for people to submit ideas

Two more will be added soon
- newsletter: storing newsletter information for subscribers
- join: storing member form submissions

Each application has a templates and static directory, for holding html templates and other static data (assets, css, etc). Templates can be called from between applications, and all general purpose templates will be stored in main/templates.

For a thorough understanding of Django, I highly recommend going through the [Mozilla Django tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) to get a better idea of the directory structure.
