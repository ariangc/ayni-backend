from app import db, ma
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from models.addUpdateDelete import AddUpdateDelete
from marshmallow import Schema, fields, pre_load
from marshmallow import validate
from marshmallow import Schema, fields
from marshmallow_validators.wtforms import from_wtforms
from wtforms.validators import Email, Length
from sqlalchemy import *

class Like(AddUpdateDelete, db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), unique=True)
	description = db.Column(db.String(1000))
	logodir = db.Column(db.String(500), unique=True, nullable = True)
	create_date = db.Column(db.DateTime, server_default = func.current_timestamp())
	last_mod_date = db.Column(db.DateTime, server_default = func.current_timestamp())
	
	@classmethod
	def addOne(self,obj):
		db.session.add(obj)
		db.session.commit()
		db.session.flush()
		return obj.id

class LikeSchema(ma.Schema):
	id = fields.Integer(dump_only=True)
	name = fields.String(required=True, validate=validate.Length(3))
	description = fields.String(required=True, validate=validate.Length(3))
	logodir = fields.String(required=True)
<<<<<<< HEAD
	url = ma.URLFor('api.likesresource', id='<id>', _external=True)
=======
	url = ma.URLFor('api.likesresource', id='<id>', _external=True)
>>>>>>> e79e45981aaf7e9234a797f80c7e2f3fde42af7f
