from functools import wraps

from flask import render_template, Blueprint
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import redirect

from app.forms.LoginForm import LoginForm
from app.models.User import User

module = Blueprint('auth', __name__)


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('auth.login'))
    return wrap


@module.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        session.pop('user', None)
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        print(generate_password_hash('aaAA123456'))
        if user and check_password_hash(user.password, password):
            session['user'] = user.id
            return redirect(url_for('default.default'))
        else:
            error = 'Hatalı giriş bilgileri'
            return render_template('login.html', error=error, form=form)
    return render_template('login.html', form=form)


@module.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')