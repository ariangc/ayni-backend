from models.like import Like, LikeSchema
from models.like_x_user import Like_x_User, Like_X_UserSchema 
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

def jsonifyLike(like):
    e = {}
    e['id'] = like.id
    e['name'] = like.name
    e['description'] = like.description
    e['logodir'] = like.logodir
    return e

def getAllLikes():
    get = Like.query.all()
    d = {}
    list = []
    for i in get:
        list.append(jsonifyLike(i))
    d['listOfLikes'] = list
    return d, status.HTTP_200_OK

def addLikeXUser(userId, likeId):
    obj = Like_x_User(
        id_user = userId,
        id_like = likeId,
        flg_active = 1
        )
    obj = Like_x_User.addOne(obj)
    return 1
    
        
def addLikesXUser(userId, listOfidLikes):
    for i in listOfidLikes:
        addLikeXUser(userId, i)
    return status.HTTP_200_OK

def getLikesXUser(userId):
    subOne = Like_x_User.query.filter(Like_x_User.id_user == userId, Like_x_User.flg_active == 1).subquery()
    subTwo = db.session.query(Like).join(subOne).filter(Like.id == subOne.c.id_like).all()
    list = []
    d = {}
    for i in subTwo:
        list.append(jsonifyLike(i))
    d['listOfLikes'] = list
    return d, status.HTTP_200_OK

def updateLikesXUser(userId, listOnLikes, listOffLikes):
    for i in listOnLikes:
        exists, isActive = Like_x_User.verifyExistActive(userId, i)
        if not exists:
            addLikeXUser(userId, i)
        if exists and not isActive:
            Like_x_User.turnFlg(userId, i)
    for j in listOffLikes:
        exists, isActive = Like_x_User.verifyExistActive(userId, j)
        if exists and isActive:
            Like_x_User.turnFlg(userId, j)
    return status.HTTP_200_OK


