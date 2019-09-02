from models.user import User, UserSchema
from models.activity import Activity
from models.enrollment import Enrollment
from resources.security import AuthRequiredResource
from flask_restful import Resource
import status

user_schema = UserSchema()

class UserResource(AuthRequiredResource):
	def get(self, id):
		try:
			user = User.query.get_or_404(id)
			d = {}
			d['username'] = user.username
			d['name'] = user.name
			d['id'] = user.id
			d['contact'] = {'email': user.email, 'facebook': user.facebook, 'linkedin': user.linkedin }
			d['description'] = user.description
			d['membership'] = user.membership
			d['points'] = user.points
			d['recentActivities'] = []
			d['nEnrollments'] = Enrollment.query.filter(Enrollment.user_id == user.id).count()
			d['nOrganized'] = Activity.query.filter(Activity.user_id == user.id).count()
			d['url'] = user_schema.dump(user).data['url']

			recentActivities = Enrollment.query.filter(Enrollment.user_id == user.id)[-3:]
			for recentActivity in recentActivities:
				e = {}
				activityData = Activity.query.filter(Activity.id == recentActivity.activity_id).all()[0]
				e['title'] = activityData.title
				e['description'] = activityData.description
				e['imgUrl'] = 'https://cdn1.soyunperro.com/wp-content/uploads/2018/01/Akita-Inu-perro.jpg'
				e['id'] = activityData.id
				d['recentActivities'].append(e)
			return d, status.HTTP_200_OK
		except SQLAlchemyError as e:
			db.session.rollback()
			response = {'error': str(e)}
			return response, status.HTTP_400_BAD_REQUEST

class UserListResource(AuthRequiredResource):
	def get(self):
		try:
			users = User.query.all()
			d = []
			for user in users:
				e = {}
				e['username'] = user.username
				e['name'] = user.name
				e['id'] = user.id
				e['contact'] = {'email': user.email, 'facebook': user.facebook, 'linkedin': user.linkedin }
				e['description'] = user.description
				e['membership'] = user.membership
				e['points'] = user.points
				e['recentActivities'] = []
				e['nEnrollments'] = Enrollment.query.filter(Enrollment.user_id == user.id).count()
				e['nOrganized'] = Activity.query.filter(Activity.user_id == user.id).count()
				e['url'] = user_schema.dump(user).data['url']

				recentActivities = Enrollment.query.filter(Enrollment.user_id == user.id)[-3:]
				for recentActivity in recentActivities:
					e2 = {}
					activityData = Activity.query.filter(Activity.id == recentActivity.activity_id).all()[0]
					e2['title'] = activityData.title
					e2['description'] = activityData.description
					e2['imgUrl'] = 'https://cdn1.soyunperro.com/wp-content/uploads/2018/01/Akita-Inu-perro.jpg'
					e2['id'] = activityData.id
					e['recentActivities'].append(e2)
				
				d.append(e)
			return d, status.HTTP_200_OK
		except SQLAlchemyError as e:
			db.session.rollback()
			response = {'error': str(e)}
			return response, status.HTTP_400_BAD_REQUEST
		return result