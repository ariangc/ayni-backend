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
from models.user import User
##

class Points(AddUpdateDelete, db.Model):
    __tablename__='points'
    user_id = db.Column(db.Integer, ForeignKey('user.id'), primary_key = True)
    send_user_id = db.Column(db.Integer, ForeignKey('user.id'), primary_key = True) #el que envio los puntos
    quantity = db.Column(db.Integer, nullable = False)
    content = db.Column(db.String(255), nullable = False)
    send_date = db.Column(db.DateTime, server_default = func.current_timestamp(), nullable = False)

    @classmethod
    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        return 1

#class PointsSchema(ma.Schema):
	##
    #url = ma.URLFor('api.likes_x_userresource', id='<id>', _external=True)
