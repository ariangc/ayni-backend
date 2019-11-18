from flask import Blueprint
from flask_restful import Api, Resource

<<<<<<< HEAD

# *********** Models *********** #
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

# *********** Resources *********** #
=======
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
>>>>>>> e79e45981aaf7e9234a797f80c7e2f3fde42af7f
from resources.user import UserListResource, UserResource
from resources.authentication import SignupResource, LoginResource
from resources.activity import *
from resources.news import NewsResource, NewsListResource
from resources.schedule import ScheduleResource, ScheduleListResource
from resources.enrollment import EnrollmentResource, EnrollmentListResource
<<<<<<< HEAD
from resources.likeRSC import AddLikeResource, GetAllLikes, PostLikesXUser, GetLikesXUser, UpdateLikesXUser
from resources import organizationRSC
from resources import projectRSC
=======
from resources.likeRSC import AddLikeResource
>>>>>>> e79e45981aaf7e9234a797f80c7e2f3fde42af7f

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# *********** Services *********** #

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
<<<<<<< HEAD

# *********** Likes *********** #
api.add_resource(AddLikeResource, '/like/add')
api.add_resource(GetAllLikes, '/like/get_all')
api.add_resource(PostLikesXUser, '/like/post_likes')
api.add_resource(GetLikesXUser, '/like/get_likes_user')
api.add_resource(UpdateLikesXUser, '/like/update_likes_user')

# *********** Organization *********** #
api.add_resource(organizationRSC.CreateOrganization, '/organization/create')
api.add_resource(organizationRSC.UpdateMembers, '/organization/update_users')
api.add_resource(organizationRSC.GetOrganizationsXUser, '/organization/get_org_user')
api.add_resource(organizationRSC.DeleteOrganization, '/organization/delete')

# *********** Project *********** #
api.add_resource(projectRSC.CreateProject, '/project/create')
api.add_resource(projectRSC.DeleteProject, '/project/delete')
api.add_resource(projectRSC.GetProjectXOrganization, '/project/get_project_organization')


=======
api.add_resource(AddLikeResource, '/like/add')
>>>>>>> e79e45981aaf7e9234a797f80c7e2f3fde42af7f
