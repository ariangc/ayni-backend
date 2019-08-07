from flask import Blueprint
from flask_restful import Api, Resource

# Importing Resources from resources/
from resources.user import UserListResource, UserResource
from resources.authentication import SignupResource, LoginResource
from resources.activity import *
from resources.news import NewsResource, NewsListResource
from resources.schedule import ScheduleResource, ScheduleListResource
from resources.enrollment import EnrollmentResource, EnrollmentListResource

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
api.add_resouce(GetClosetsActivities, '/activities/close/')