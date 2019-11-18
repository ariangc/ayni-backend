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
from models.organization import Organization
##

class Project(AddUpdateDelete, db.Model):
    ## aqui las notitas de cada tipo por cada actividad
    __tablename__='project'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    organization_id = db.Column(db.Integer, ForeignKey('organization.id'), primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    created_date = db.Column(db.DateTime, server_default = func.current_timestamp(), nullable = False)
    flg_active = db.Column(db.Integer, nullable = False, default = 1)
    image_direction = db.Column(db.String(255))

    @classmethod
    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        return 1
    
    @classmethod
    def turnFlg(self, projectId):
        ver = Project.query.filter(Project.id == projectId).first()
        ver.flg_active = 1 - ver.flg_active
        db.session.commit()
        return 1

#class Staff_x_ActivitySchema(ma.Schema):
	##
    #url = ma.URLFor('api.likes_x_userresource', id='<id>', _external=True)
