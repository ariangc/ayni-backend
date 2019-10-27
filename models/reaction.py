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
from models.news import News
from models.user import User
##

class Reaction(AddUpdateDelete, db.Model):
    ## aqui las notitas de cada tipo por cada actividad
    __tablename__='coments'
    id = db.Column(db.Integer, primary_key = True)
    news_id = db.Column(db.Integer, ForeignKey('news.id'), primary_key = True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), primary_key = True)
    publication_date = db.Column(db.DateTime, server_default = func.current_timestamp(), nullable = False)
    type = db.Column(db.Integer, nullable = False)

    @classmethod
    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        return 1

#class ReactionSchema(ma.Schema):
	##
    #url = ma.URLFor('api.likes_x_userresource', id='<id>', _external=True)
