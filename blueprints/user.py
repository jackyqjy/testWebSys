from flask import Blueprint, render_template

bp = Blueprint("user", __name__, url_prefix="/user")

@bp.route("/register")
def register():
    return render_template("front/register.html")