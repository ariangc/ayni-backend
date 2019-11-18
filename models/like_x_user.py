from app import db, ma
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from models.addUpdateDelete import AddUpdateDelete
from models.like import Like
from models.user import User
from marshmallow import Schema, fields, pre_load
from marshmallow import validate
from marshmallow import Schema, fields
from marshmallow_validators.wtforms import from_wtforms
from wtforms.validators import Email, Length
from sqlalchemy import *

<<<<<<< HEAD
class Like_x_User(AddUpdateDelete, db.Model):
=======
class Like_X_User(AddUpdateDelete, db.Model):
>>>>>>> e79e45981aaf7e9234a797f80c7e2f3fde42af7f
    __tablename__='like_x_user'
    id_user = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    id_like = db.Column(db.Integer, ForeignKey('like.id'), primary_key=True)
    flg_active = db.Column(db.Integer, nullable = False)
    last_mod_date = db.Column(db.DateTime, server_default = func.current_timestamp())

    @classmethod
    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        return 1

<<<<<<< HEAD
    @classmethod
    def verifyExistActive(self, userId, likeId):
        ver = Like_x_User.query.filter(Like_x_User.id_user == userId, Like_x_User.id_like == likeId).first()
        if ver is None:
            return False, False
        if ver.flg_active == 1:
            return True, True
        return True, False
        
    @classmethod
    def turnFlg(self, userId, likeId):
        ver = Like_x_User.query.filter(Like_x_User.id_user == userId, Like_x_User.id_like == likeId).first()
        ver.flg_active = 1 - ver.flg_active
        db.session.commit()
        return 1

=======
>>>>>>> e79e45981aaf7e9234a797f80c7e2f3fde42af7f
class Like_X_UserSchema(ma.Schema):
	id_user = fields.Integer(required=True)
	id_like = fields.Integer(required=True)
	flg_activate = fields.Integer(required=True)
	#url = ma.URLFor('api.likes_x_userresource', id='<id>', _external=True)
