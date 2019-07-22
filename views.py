from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from app import db
from sqlalchemy.exc import SQLAlchemyError
from flask_login import login_user, logout_user, login_required, current_user
import status
from flask_httpauth import HTTPBasicAuth
from flask import g
from models import User, UserSchema

api_bp = Blueprint('api', __name__)
user_schema = UserSchema()
api = Api(api_bp)

class UserResource(Resource):
	@login_required
	def get(self, id):
		user = User.query.get_or_404(id)
		result = user_schema.dump(user).data
		return result

class UserListResource(Resource):
	@login_required
	def get(self):
		users = User.query.all()
		result = user_schema.dump(users, many=True).data
		return result

	@login_required
	def post(self):
		request_dict = request.get_json()
		if not request_dict:
			response = {'user': 'No input data provided'}
			return response, status.HTTP_400_BAD_REQUEST
		errors = user_schema.validate(request_dict)
		if errors:
			return errors, status.HTTP_400_BAD_REQUEST
		name = request_dict['name']
		username = request_dict['username']
		email = request_dict['email']
		existing_user = User.query.filter_by(username=username).first()

		if existing_user is not None:
			response = {'user': 'An user with the same username already exists'}
			return response, status.HTTP_400_BAD_REQUEST
		try:
			user = User(name=name, username=username, email=email)
			error_message, password_ok = \
				user.check_password_strength_and_hash_if_ok(request_dict['password'])
			if password_ok:
				user.add(user)
				query = User.query.get(user.id)
				result = user_schema.dump(query).data
				return result, status.HTTP_201_CREATED
			else:
				return {"error": error_message}, status.HTTP_400_BAD_REQUEST
		except SQLAlchemyError as e:
			db.session.rollback()
			resp = {"error": str(e)}
			return resp, status.HTTP_400_BAD_REQUEST

api.add_resource(UserListResource, '/users/')
api.add_resource(UserResource, '/users/<int:id>')
