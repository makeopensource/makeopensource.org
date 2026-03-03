from flask import Blueprint, render_template

general_bp = Blueprint("general", __name__)


@general_bp.get("/")
def index():
    return render_template("general/homepage.html")
