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
##

class Kanban(AddUpdateDelete, db.Model):
	##aqui deberian ir los tres tipos, to do, doing y done
	__tablename__='kanban'
	id = db.Column(db.Integer, primary_key = True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(255), nullable = False)

	@classmethod
	def addOne(self,obj):
		db.session.add(obj)
		db.session.commit()
		db.session.flush()
		return 1

#class KanbanSchema(ma.Schema):
	##
	#url = ma.URLFor('api.likes_x_userresource', id='<id>', _external=True)
