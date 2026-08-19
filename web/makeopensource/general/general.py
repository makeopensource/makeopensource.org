from flask import Blueprint, render_template, redirect

general_bp = Blueprint("general", __name__)


@general_bp.get("/")
def index():
    return render_template("general/homepage.html")


@general_bp.get("/discord/")
def discord():
    return redirect("https://discord.com/invite/xbBPqdqr6n")
