from app import db, ma
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from models.addUpdateDelete import AddUpdateDelete
from marshmallow import Schema, fields, pre_load
from marshmallow import validate
from marshmallow import Schema, fields
from marshmallow_validators.wtforms import from_wtforms
from wtforms.validators import Email, Length
from sqlalchemy import *
##
from models.kanban import Kanban
from models.activity import Activity
##

class Task(AddUpdateDelete, db.Model):
	## aqui las notitas de cada tipo por cada actividad
	__tablename__='task'
	id = db.Column(db.Integer, primary_key = True, autoincrement=True)
	project_id = db.Column(db.Integer, db.ForeignKey('project.id'), primary_key = True)
	creation_date = db.Column(db.DateTime, server_default = func.current_timestamp(), nullable = False)
	name = db.Column(db.String(100), nullable = False)
	description = db.Column(db.String(255))
	modification_date = db.Column(db.DateTime, server_default = func.current_timestamp(), nullable = False)
	init_date = db.Column(db.DateTime)
	finish_date = db.Column(db.DateTime)
	
	@classmethod
	def addOne(self,obj):
		db.session.add(obj)
		db.session.commit()
		db.session.flush()
		return 1

#class Kanban_x_ActivitySchema(ma.Schema):
	##
	#url = ma.URLFor('api.likes_x_userresource', id='<id>', _external=True)
