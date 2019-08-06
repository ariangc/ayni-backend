from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from resources.utils import password_policy
from flask import request, jsonify, make_response, g
from app import db
from resources.user import user_schema
import status
from flask_restful import Resource


class SignupResource(Resource):
	def post(self):
		request_dict = request.get_json()
		if not request_dict:
			response = {'user': 'No input data provided'}
			return response, status.HTTP_400_BAD_REQUEST

		errors = user_schema.validate(request_dict)
		if errors:
			return errors, status.HTTP_400_BAD_REQUEST

		email = request_dict['email']
		name = request_dict['name']
		username = request_dict['username']
		password = request_dict['password']

		user_email = User.query.filter_by(email=email).first()
		user_username = User.query.filter_by(username=username).first()
		
		#Check if user with same email exists
		if user_email:
			resp = {"error": "Email address already exists."}
			return resp, status.HTTP_400_BAD_REQUEST
		
		#Check if user with same username exists
		if user_username:
			resp = {"error": "Username already exists."}
			return resp, status.HTTP_400_BAD_REQUEST

		#Check password strength
		if len(password_policy.test(password)):
			resp = {"error": "Please check password strength. It should have at least 5 characters, 1 uppercase letter, 1 number and 1 special character."}
			return resp, status.HTTP_400_BAD_REQUEST

		new_user = User(email=email, name=name, username=username, password=generate_password_hash(password, method='sha256'))

		db.session.add(new_user)
		db.session.commit()

		user = User.query.filter_by(email=email).first()
		g.user = user
		token = g.user.generate_auth_token()
		userdata = user_schema.dump(g.user).data
		resp = {'token' : token.decode('ascii')}
		resp.update(userdata)
		return resp, status.HTTP_200_OK

class LoginResource(Resource):
	def post(self):
		request_dict = request.get_json()
		if not request_dict:
			response = {'error': 'No input data provided'}
			return response, status.HTTP_400_BAD_REQUEST

		email = request_dict['email']
		password = request_dict['password']
		remember = True if request_dict['remember'] else False

		user = User.query.filter_by(email=email).first()

		if not user or not check_password_hash(user.password, password):
			resp = {'error': 'Please check your login credentials and try again.'}
			return resp, status.HTTP_400_BAD_REQUEST
		g.user = user
		token = g.user.generate_auth_token()
		userdata = user_schema.dump(g.user).data
		resp = {'token' : token.decode('ascii')}
		resp.update(userdata)
		return resp, status.HTTP_200_OK
