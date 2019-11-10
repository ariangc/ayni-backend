#from marshmallow import Schema, fields, pre_load
from marshmallow import validate
from marshmallow import Schema, fields
from marshmallow_validators.wtforms import from_wtforms
from wtforms.validators import Email, Length
from flask_login import UserMixin
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from app import db, ma
from config import SECRET_KEY
from passlib.apps import custom_app_context as password_context
import re
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from models.addUpdateDelete import AddUpdateDelete

''' User '''
locales = ['es_ES', 'es']

class User(UserMixin, AddUpdateDelete, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), unique=True)
	username = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	name = db.Column(db.String(100))
	flg_special_user = db.Column(db.Integer, default = 0, nullable = False)
	telephone_number_1 = db.Column(db.String(20))
	telephone_number_2 = db.Column(db.String(20))
	email_1 = db.Column(db.String(50))
	email_2 = db.Column(db.String(50))
	direction = db.Column(db.String(100))

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