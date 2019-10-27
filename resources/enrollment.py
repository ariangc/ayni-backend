from models.enrollment import Enrollment, EnrollmentSchema
from resources.security import AuthRequiredResource
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError
from app import db
import status
from flask import request

enrollment_schema = EnrollmentSchema()

class EnrollmentResource(AuthRequiredResource):
	def get(self, id):
		enrollment = Enrollment.query.get_or_404(id)
		result = enrollment_schema.dump(enrollment).data
		return result

class EnrollmentListResource(AuthRequiredResource):
	def get(self):
		enrollments = Enrollment.query.all()
		result = enrollment_schema.dump(enrollments, many=True).data
		return result

	def post(self):
		request_dict = request.get_json()
		if not request_dict:
			response = {'error': 'No input data provided'}
			return response, status.HTTP_400_BAD_REQUEST
		errors = enrollment_schema.validate(request_dict)
		if errors:
			return errors, status.HTTP_400_BAD_REQUEST
		try:
			user_id = request_dict['user_id']
			activity_id = request_dict['activity_id']
			enrollment = Enrollment(user_id=user_id, activity_id=activity_id)
			enrollment.add(enrollment)
			query = Enrollment.query.get(enrollment.id)
			result = enrollment_schema.dump(query).data
			return result, status.HTTP_201_CREATED
		except SQLAlchemyError as e:
			db.session.rollback()
			response = {'error': str(e)}
			return response, status.HTTP_400_BAD_REQUEST