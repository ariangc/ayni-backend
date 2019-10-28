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
from models.organization import Organization
##

class User_x_Organization(AddUpdateDelete, db.Model):
    ## aqui las notitas de cada tipo por cada actividad
    __tablename__='user_x_organization'
    organization_id = db.Column(db.Integer, ForeignKey('organization.id'), primary_key = True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False, primary_key = True)
    flg_active = db.Column(db.Integer, nullable = False, default = 1)

    @classmethod
    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        return 1

#class Staff_x_ActivitySchema(ma.Schema):
	##
    #url = ma.URLFor('api.likes_x_userresource', id='<id>', _external=True)
