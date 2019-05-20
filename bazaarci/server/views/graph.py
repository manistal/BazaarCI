
from flask import Blueprint, render_template, request

bp = Blueprint('graph', __name__)

@bp.route('/')
def index():
    return render_template('graph.html')


