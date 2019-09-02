from models.user import User
from models.enrollment import Enrollment
from models.activity import Activity
from werkzeug.security import generate_password_hash, check_password_hash
from resources.utils import password_policy
from flask import request, jsonify, make_response, g
from app import db
from resources.user import user_schema
from resources.security import verify_password
import status
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError

class SignupResource(Resource):
	def post(self):
		request_dict = request.get_json()
		if not request_dict:
			response = {'error': 'No input data provided'}
			return response, status.HTTP_400_BAD_REQUEST

		errors = user_schema.validate(request_dict)
		if errors:
			errors.update({'error':'Some fields are invalid'})
			return errors, status.HTTP_400_BAD_REQUEST

		email = request_dict['email']
		name = request_dict['name']
		username = request_dict['username']
		password = request_dict['password']
		membership = request_dict['membership']

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

		new_user = User(email=email, name=name, username=username, password=generate_password_hash(password, method='sha256'), points=0, membership=membership)

		try:
			db.session.add(new_user)
			db.session.commit()

			user = User.query.filter_by(email=email).first()
			g.user = user
			token = g.user.generate_auth_token()
			
			d = {}
			
			d['username'] = user.username
			d['name'] = user.name
			d['id'] = user.id
			d['contact'] = {'email': user.email, 'facebook': user.facebook, 'linkedin': user.linkedin }
			d['description'] = user.description
			d['membership'] = user.membership
			d['points'] = user.points
			d['recentActivities'] = []
			d['nEnrollments'] = 0
			d['nOrganized'] = 0 
			d['url'] = user_schema.dump(user).data['url']

			resp = {'token' : token.decode('ascii')}
			resp.update(d)
			return resp, status.HTTP_200_OK
		except SQLAlchemyError as e:
			db.session.rollback()
			response = {'error': str(e)}
			return response, status.HTTP_400_BAD_REQUEST

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
		d = {}
		d['username'] = user.username
		d['name'] = user.name
		d['id'] = user.id
		d['contact'] = {'email': user.email, 'facebook': user.facebook, 'linkedin': user.linkedin }
		d['description'] = user.description
		d['membership'] = user.membership
		d['points'] = user.points
		d['recentActivities'] = []
		d['nEnrollments'] = Enrollment.query.filter(Enrollment.user_id == user.id).count()
		d['nOrganized'] = Activity.query.filter(Activity.user_id == user.id).count()
		d['url'] = user_schema.dump(user).data['url']

		recentActivities = Enrollment.query.filter(Enrollment.user_id == user.id)[-3:]
		for recentActivity in recentActivities:
			activityData = Activity.query.filter(Activity.id == recentActivity.activity_id).all()[0]
			e = {}
			e['title'] = activityData.title
			e['description'] = activityData.description
			e['imgUrl'] = 'https://cdn1.soyunperro.com/wp-content/uploads/2018/01/Akita-Inu-perro.jpg'
			e['id'] = activityData.id
			d['recentActivities'].append(e)
		resp = {'token' : token.decode('ascii')}
		resp.update(d)
		return resp, status.HTTP_200_OK

class VerifyTokenResource(Resource):
	def get(self):
		request_dict = request.get_json()
		if not request_dict:
			response = {'error': 'No input data provided'}
			return response, status.HTTP_400_BAD_REQUEST
		
		token = request_dict['token']
		valid = verify_password(token, "unused")
		resp = {'valid': valid}
		return resp, status.HTTP_200_OK