from flask import Blueprint
from flask_restful import Api, Resource

from models.chat import Chat
from models.comments import Comments
from models.contact import Contact
from models.kanban import Kanban
from models.kanban_x_activity import Kanban_x_Activity
from models.message import Message
from models.notification_type import Notification_Type
from models.notification import Notification
from models.points import Points
from models.reaction import Reaction
from models.report import Report
from models.staff_x_activity import Staff_x_Activity

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
