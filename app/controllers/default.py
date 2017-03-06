from flask import render_template, Blueprint
from app.controllers.auth import login_required

module = Blueprint('default', __name__)


@module.route('/')
@login_required
def default():
    return render_template('index.html')