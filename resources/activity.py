from models import Activity, ActivitySchema
from resources.security import AuthRequiredResource
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError
from app import db
import status
from flask import request

activity_schema = ActivitySchema()

class ActivityResource(AuthRequiredResource):
	def get(self, id):
		activity = Activity.query.get_or_404(id)
		result = activity_schema.dump(activity).data
		return result

	def patch(self, id):
		activity = Activity.query.get_or_404(id)
		request_dict = request.get_json(force=True)
		if 'title' in request_dict:
			title = request_dict['title']
			if Activity.is_unique(id=id, title=title):
				activity.title = title
			else:
				response = {'error': 'An activity with the same title already exists'}
				return response, status.HTTP_400_BAD_REQUEST
		
		if 'description' in request_dict:
			activity.description = request_dict['description']
		if 'latitude' in request_dict:
			activity.latitude = request_dict['latitude']
		if 'longitude' in request_dict:
			activity.longitude = request_dict['longitude']
		if 'user_id' in request_dict:
			activity.user_id = request_dict['user_id']

		dumped_activity, dump_errors = activity_schema.dump(activity)
		print(dumped_activity)
		if dump_errors:
			return dump_errors, status.HTTP_400_BAD_REQUEST
		validate_errors = activity_schema.validate(dumped_activity)
		if validate_errors:
			return validate_errors, status.HTTP_400_BAD_REQUEST
		try:
			activity.update()
			result = activity_schema.dump(activity).data
			return result, status.HTTP_200_OK
		except SQLAlchemyError as e:
			db.session.rollback()
			resp = {"error": str(e)}
			return resp, status.HTTP_400_BAD_REQUEST

class ActivityListResource(AuthRequiredResource):
	def get(self):
		activities = Activity.query.all()
		result = activity_schema.dump(activities, many=True).data
		return result

	def post(self):
		request_dict = request.get_json()
		if not request_dict:
			response = {'error': 'No input data provided'}
			return response, status.HTTP_400_BAD_REQUEST
		errors = activity_schema.validate(request_dict)
		if errors:
			return errors, status.HTTP_400_BAD_REQUEST

		try:
			title = request_dict['title']
			if not Activity.is_unique(id=id, title=title):
				response = {'error': 'An activity with the same title already exists'}
				return response, status.HTTP_400_BAD_REQUEST
			description = request_dict['description']
			latitude = request_dict['latitude']
			longitude = request_dict['longitude']
			user_id = request_dict['user_id']

			activity = Activity(title=title, description=description, latitude=latitude, \
								longitude=longitude, user_id=user_id)
			activity.add(activity)
			query = Activity.query.get(activity.id)
			result = activity_schema.dump(query).data
			return result, status.HTTP_201_CREATED
		except SQLAlchemyError as e:
			db.session.rollback()
			response = {'error': str(e)}
			return response, status.HTTP_400_BAD_REQUEST
