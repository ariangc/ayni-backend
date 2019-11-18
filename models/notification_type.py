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

class Notification_Type(AddUpdateDelete, db.Model):
    __tablename__='notification_type'
<<<<<<< HEAD
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
=======
    id = db.Column(db.Integer, primary_key=True)
>>>>>>> e79e45981aaf7e9234a797f80c7e2f3fde42af7f
    type = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(255), nullable = False)
    content = db.Column(db.String(255), nullable = False)

    @classmethod
    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        return 1

class Notification_TypeSchema(ma.Schema):
	id = fields.Integer(required=True)
	type = fields.String(required=True)
	description = fields.String(required=True)
    #content = fields.String(required=True)
	#url = ma.URLFor('api.likes_x_userresource', id='<id>', _external=True)
