
from flask import Blueprint, redirect, url_for, request, render_template, flash

from flask_login import LoginManager, login_required, login_user, logout_user

from models.users import User

from database.config import session
from sqlalchemy import select



login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.find(id=user_id)

user_bp = Blueprint(name='user', import_name=__name__, template_folder='templates', url_prefix='/user')

@user_bp.route('/', methods=['POST', 'GET'])
def view():
    users = session.scalars(select(User)).all()
    return render_template('users/view.html', users = users)