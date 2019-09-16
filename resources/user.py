from models.user import User, UserSchema
from resources.security import AuthRequiredResource
from flask_restful import Resource

user_schema = UserSchema()

class UserResource(AuthRequiredResource):
	def get(self, id):
		user = User.query.get_or_404(id)
		result = user_schema.dump(user).data
		return result

class UserListResource(AuthRequiredResource):
	def get(self):
		users = User.query.all()
		result = user_schema.dump(users, many=True).data
		return result