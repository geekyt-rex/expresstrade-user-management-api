from sqlalchemy import or_

from models.user_model import User
from database.db import db

from utils.validators import validate_user_data

from flask_jwt_extended import create_access_token

# CREATE USER

def create_user_service(data):

    is_valid, error = validate_user_data(data)

    if not is_valid:

        return {
            "success": False,
            "error": error
        }, 400

    existing_user = User.query.filter_by(
        email=data["email"]
    ).first()

    if existing_user:

        return {
            "success": False,
            "error": "Email already exists"
        }, 409

    new_user = User(
        name=data["name"],
        email=data["email"],
        role=data["role"]
    )

    db.session.add(new_user)

    db.session.commit()

    return {
        "success": True,
        "message": "User created successfully",
        "user": new_user.to_dict()
    }, 201

# GET ALL USERS

def get_all_users_service(search, page, limit):

    query = User.query

    # SEARCH

    if search:

        query = query.filter(
            or_(
                User.name.ilike(f"%{search}%"),
                User.email.ilike(f"%{search}%")
            )
        )

    # PAGINATION

    paginated_users = query.paginate(
        page=page,
        per_page=limit,
        error_out=False
    )

    users = []

    for user in paginated_users.items:

        users.append(
            user.to_dict()
        )

    return {
        "success": True,
        "page": page,
        "limit": limit,
        "total_users": paginated_users.total,
        "users": users
    }, 200

# GET USER BY ID

def get_user_by_id_service(user_id):

    user = User.query.get(user_id)

    if not user:

        return {
            "success": False,
            "error": "User not found"
        }, 404

    return {
        "success": True,
        "user": user.to_dict()
    }, 200


def login_user_service(data):

    email = data.get("email")

    if not email:

        return {
            "success": False,
            "error": "Email is required"
        }, 400

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:

        return {
            "success": False,
            "error": "Invalid email"
        }, 401

    access_token = create_access_token(
        identity=str(user.id)
    )

    return {
        "success": True,
        "access_token": access_token
    }, 200