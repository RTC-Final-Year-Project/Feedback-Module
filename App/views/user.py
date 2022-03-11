from flask import Blueprint, render_template, jsonify, request
from flask_jwt import jwt_required


from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')


# @user_views.route('/users')
# def get_users():
#     users = get_all_users()
#     return jsonify(serialize_list(users))


@user_views.route('/api/users')
def get_users():
    return jsonify(get_all_users_json())