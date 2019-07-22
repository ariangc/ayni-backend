from marshmallow import Schema, fields, pre_load
from marshmallow import validate
from flask_login import UserMixin
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from app import db
from passlib.apps import custom_app_context as password_context
import re

ma = Marshmallow()

class AddUpdateDelete():
	def add(self, resource):
		db.session.add(resource)
		return db.session.commit()
	
	def update(self):
		return db.session.commit()
	
	def delete(self, resource):
		db.session.delete(resource)
		return db.session.commit()

class User(UserMixin, AddUpdateDelete, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), unique=True)
	username = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	name = db.Column(db.String(100))

	def check_password_strength_and_hash_if_ok(self, password):
		if len(password) < 8:
			return 'The password is too short', False
		if len(password) > 32:
			return 'The password is too long', False
		if re.search(r'[A-Z]', password) is None:
			return 'The password must include at least one uppercase letter', False
		if re.search(r'[a-z]', password) is None:
			return 'The password must include at least one lowercase letter', False
		if re.search(r'\d', password) is None:
			return 'The password must include at least one number', False
		if re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None:
			return 'The password must include at least one symbol', False
		self.hashed_password = password_context.encrypt(password)
		return '', True

class UserSchema(ma.Schema):
	id = fields.Integer(dump_only=True)
	name = fields.String(required=True, validate=validate.Length(3))
	username = fields.String(required=True, validate=validate.Length(3))
	email = fields.String(required=True, validate=validate.Length(3)) #Cambiar validaciones pls
	url = ma.URLFor('api.userresource', id='<id>', _external=True)
