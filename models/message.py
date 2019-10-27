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

class Message(AddUpdateDelete, db.Model):
    __tablename__='message'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False, primary_key = True)
    chat_id = db.Column(db.Integer, ForeignKey('chat.id'), nullable = False, primary_key = True)
    send_date = db.Column(db.DateTime, server_default = func.current_timestamp(), nullable = False)
    content = db.Column(db.String(255), nullable = False)
    flg_visible_sender = db.Column(db.Integer, nullable = False, default = 1)
    flg_visible_receiver = db.Column(db.Integer, nullable = False, default = 1)

    @classmethod
    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        return 1

#class MessageSchema(ma.Schema):
	##
    #url = ma.URLFor('api.likes_x_userresource', id='<id>', _external=True)
