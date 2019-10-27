from models.like import Like, LikeSchema
from models.like_x_user import Like_X_User, Like_X_UserSchema 
import status
from app import db

def addLike(name, description, logodir):
    ver_name = Like.query.filter_by(name = name).first()

    if ver_name:
        resp = {"error": "Name for like already exists."}
        return resp, status.HTTP_400_BAD_REQUEST

    obj = Like(
        name = name,
        description = description,
        logodir = logodir
    )

    id_obj = Like.addOne(obj)

    return {"id": id_obj}, status.HTTP_200_OK