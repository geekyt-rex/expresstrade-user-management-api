from flask import Blueprint
from flask import request

from flask_jwt_extended import jwt_required

from services.user_service import (
    create_user_service,
    get_all_users_service,
    get_user_by_id_service,
    login_user_service
)

user_bp = Blueprint(
    "user_bp",
    __name__
)

@user_bp.route("/")
def home():

    return {
        "message": "API working"
    }

# CREATE USER

@user_bp.route("/users", methods=["POST"])
def create_user():

    data = request.get_json()

    response, status_code = create_user_service(data)

    return response, status_code

# GET ALL USERS

@user_bp.route("/users", methods=["GET"])
def get_users():

    search = request.args.get("search")

    page = request.args.get(
        "page",
        default=1,
        type=int
    )

    limit = request.args.get(
        "limit",
        default=10,
        type=int
    )

    response, status_code = get_all_users_service(
        search,
        page,
        limit
    )

    return response, status_code

# GET USER BY ID

@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):

    response, status_code = get_user_by_id_service(
        user_id
    )

    return response, status_code

# LOGIN

@user_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    response, status_code = login_user_service(
        data
    )

    return response, status_code

# PROTECTED ROUTE

@user_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():

    return {
        "success": True,
        "message": "Protected route accessed"
    }, 200