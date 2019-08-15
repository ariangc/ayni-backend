from marshmallow import Schema, fields, pre_load
from marshmallow import validate
from marshmallow import Schema, fields
from marshmallow_validators.wtforms import from_wtforms
from wtforms.validators import Email, Length
from flask_login import UserMixin
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from app import db
from config import SECRET_KEY
from passlib.apps import custom_app_context as password_context
import re
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

''' User '''

class User(UserMixin, AddUpdateDelete, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), unique=True)
	username = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	name = db.Column(db.String(100))
	enrollment = db.relationship("Enrollment")
	activities = db.relationship("Activity")
	
	def generate_auth_token(self, expiration = 600):
		s = Serializer(SECRET_KEY, expires_in = expiration)
		return s.dumps({ 'id': self.id })

	@staticmethod
	def verify_auth_token(token):
		print("Verificando token...")
		s = Serializer(SECRET_KEY)
		try:
			data = s.loads(token)
		except SignatureExpired:
			return None # valid token, but expired
		except BadSignature:
			return None # invalid token
		user = User.query.get(data['id'])
		return user

class UserSchema(ma.Schema):
	id = fields.Integer(dump_only=True)
	name = fields.String(required=True, validate=validate.Length(3))
	username = fields.String(required=True, validate=validate.Length(3))
	email = fields.String(required=True, validate=from_wtforms([Email()], locales=locales))
	url = ma.URLFor('api.userresource', id='<id>', _external=True)