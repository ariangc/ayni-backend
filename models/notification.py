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
from models.notification_type import Notification_Type
from models.user import User
##

class Notification(AddUpdateDelete, db.Model):
    __tablename__='notification'
<<<<<<< HEAD
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
=======
    id = db.Column(db.Integer, primary_key = True)
>>>>>>> e79e45981aaf7e9234a797f80c7e2f3fde42af7f
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    notification_type_id = db.Column(db.Integer, ForeignKey('notification_type.id'), nullable = False)
    description = db.Column(db.String(255), nullable = False)
    flg_seen = db.Column(db.Integer, nullable=False)
    notification_date = db.Column(db.DateTime, server_default = func.current_timestamp(), nullable = False)
    seen_date = db.Column(db.DateTime)

    @classmethod
    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        return 1

#class NotificationSchema(ma.Schema):
	##
    #url = ma.URLFor('api.likes_x_userresource', id='<id>', _external=True)
