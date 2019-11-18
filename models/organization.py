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

class Organization(AddUpdateDelete, db.Model):
    ## aqui las notitas de cada tipo por cada actividad
    __tablename__='organization'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(100), nullable = False)
    created_date = db.Column(db.DateTime, server_default = func.current_timestamp(), nullable = False)
    telephone_number_1 = db.Column(db.String(20))
    telephone_number_2 = db.Column(db.String(20))
    email_1 = db.Column(db.String(50))
    email_2 = db.Column(db.String(50))
    direction = db.Column(db.String(100))
    flg_active = db.Column(db.Integer, nullable = False, default = 1)
    image_direction = db.Column(db.String(255))
    id_creator = db.Column(db.Integer)
    reference_1 = db.Column(db.String(50), nullable = False)

    @classmethod
    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        return 1
    @classmethod
    def turnFlg(self, organizationId):
        ver = Organization.query.filter(Organization.id == organizationId).first()
        ver.flg_active = 1 - ver.flg_active
        db.session.commit()
        return 1

#class Staff_x_ActivitySchema(ma.Schema):
	##
    #url = ma.URLFor('api.likes_x_userresource', id='<id>', _external=True)
