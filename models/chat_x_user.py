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
from models.chat import Chat
from models.user import User
##

class Chat_x_User(AddUpdateDelete, db.Model):
    __tablename__='chat_x_user'
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False, primary_key = True)
    chat_id = db.Column(db.Integer, ForeignKey('chat.id'), nullable = False, primary_key = True)
    flg_visible = db.Column(db.Integer, nullable = False, default = 1)
    flg_eliminated = db.Column(db.Integer, nullable = False, default = 0)
    flg_archived = db.Column(db.Integer, nullable = False, default = 0)

    @classmethod
    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        return 1

#class Chat_x_UserSchema(ma.Schema):
	##
    #url = ma.URLFor('api.likes_x_userresource', id='<id>', _external=True)
