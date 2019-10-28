from flask import Blueprint
from flask_restful import Api, Resource

from models.project import Project
from models.activity import Activity
from models.chat import Chat
from models.chat_x_user import Chat_x_User
from models.comments import Comments
#from models.contact import Contact
from models.enrollment import Enrollment
from models.kanban import Kanban
from models.kanban_x_project import Kanban_x_Project
from models.like import Like
from models.like_x_user import Like_x_User
from models.message import Message
from models.news import News
from models.notification_type import Notification_Type
from models.notification import Notification
from models.organization import Organization
from models.points import Points
from models.reaction import Reaction
from models.report import Report
from models.schedule import Schedule
from models.staff_x_activity import Staff_x_Activity
from models.task import Task
from models.user_x_organization import User_x_Organization
from models.user import User

# Importing Resources from resources/
from resources.user import UserListResource, UserResource
from resources.authentication import SignupResource, LoginResource
from resources.activity import *
from resources.news import NewsResource, NewsListResource
from resources.schedule import ScheduleResource, ScheduleListResource
from resources.enrollment import EnrollmentResource, EnrollmentListResource
from resources.likeRSC import AddLikeResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(UserResource, '/users/<int:id>')
api.add_resource(UserListResource, '/users/')
api.add_resource(SignupResource, '/signup')
api.add_resource(LoginResource, '/login')
api.add_resource(ActivityResource, '/activities/<int:id>')
api.add_resource(ActivityListResource, '/activities/')
api.add_resource(NewsResource, '/news/<int:id>')
api.add_resource(NewsListResource, '/news/')
api.add_resource(ScheduleResource, '/schedules/<int:id>')
api.add_resource(ScheduleListResource, '/schedules/')
api.add_resource(EnrollmentResource, '/enrollments/<int:id>')
api.add_resource(EnrollmentListResource, '/enrollments/')
api.add_resource(GetClosetsActivities, '/activities/close/')
api.add_resource(AddLikeResource, '/like/add')
