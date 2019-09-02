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

ma = Marshmallow()
locales = ['es_ES', 'es']

class AddUpdateDelete():
	def add(self, resource):
		db.session.add(resource)
		return db.session.commit()
	
	def update(self):
		return db.session.commit()
	
	def delete(self, resource):
		db.session.delete(resource)
		return db.session.commit()

''' User '''

class User(UserMixin, AddUpdateDelete, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), unique=True)
	username = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	name = db.Column(db.String(100))
	enrollment = db.relationship("Enrollment")
	activities = db.relationship("Activity")
	facebook = db.Column(db.String(100), unique=True)
	linkedin = db.Column(db.String(100), unique=True)
	description = db.Column(db.String(1000))
	membership = db.Column(db.String)
	points = db.Column(db.Integer)

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
	facebook = fields.String(required=False)
	linkedin = fields.String(required=False)
	description = fields.String(required=False, validate=validate.Length(10))
	membership = fields.String(required=True) #Missing validation
	points = fields.Integer(required=False)
	url = ma.URLFor('api.userresource', id='<id>', _external=True)
	

''' Activity '''

class Activity(AddUpdateDelete, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), unique=True)
	description = db.Column(db.String(1000))
	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)
	news = db.relationship("News")
	schedules = db.relationship("Schedule")
	enrollments = db.relationship("Enrollment")
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	@classmethod
	def is_unique(cls, id, title):
		existing_activity = cls.query.filter_by(title=title).first()
		if existing_activity is None:
			return True
		else:
			if existing_activity.id == id:
				return True
			else:
				return False

class ActivitySchema(ma.Schema):
	id = fields.Integer(dump_only=True)
	title = fields.String(required=True, validate=validate.Length(3))
	description = fields.String(required=True, validate=validate.Length(3))
	latitude = fields.Float(required=True)
	longitude = fields.Float(required=True)
	user_id = fields.Integer(required=True)
	news = fields.Nested("NewsSchema", many=True, exclude=("activity",))
	schedules = fields.Nested("ScheduleSchema", many=True, exclude=("activity",))
	enrollments = fields.Nested("EnrollmentSchema", many=True, exclude=("activity",))
	url = ma.URLFor('api.activityresource', id='<id>', _external=True)

''' News '''

class News(AddUpdateDelete, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	description = db.Column(db.String(1000))
	activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))

class NewsSchema(ma.Schema):
	id = fields.Integer(dump_only=True)
	title = fields.String(required=True, validate=validate.Length(3))
	description = fields.String(required=True, validate=validate.Length(3))
	activity_id = fields.Integer(required=True)
	url = ma.URLFor('api.newsresource', id='<id>', _external=True)

''' Schedule '''

class Schedule(AddUpdateDelete, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(1000))
	start_date = db.Column(db.DateTime)
	end_date = db.Column(db.DateTime)
	activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))

class ScheduleSchema(ma.Schema):
	id = fields.Integer(dump_only=True)
	description = fields.String(required=True, validate=validate.Length(3))
	start_date = fields.DateTime(required=True)
	end_date = fields.DateTime(required=True)
	activity_id = fields.Integer(required=True)
	url = ma.URLFor('api.scheduleresource', id='<id>', _external=True)

''' Enrollment '''

class Enrollment(AddUpdateDelete, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))

class EnrollmentSchema(ma.Schema):
	id = fields.Integer(dump_only=True)
	user_id = fields.Integer(required=True)
	activity_id = fields.Integer(required=True)
