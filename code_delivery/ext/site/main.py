from flask import request, render_template
from flask import Blueprint

bp = Blueprint("site", __name__)

@bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")
