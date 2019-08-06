from models import Schedule, ScheduleSchema
from resources.security import AuthRequiredResource
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError
from app import db
import status
from flask import request

schedule_schema = ScheduleSchema()

class ScheduleResource(AuthRequiredResource):
	def get(self, id):
		schedule = Schedule.query.get_or_404(id)
		result = schedule_schema.dump(schedule).data
		return result
	
	def patch(self, id):
		schedule = Schedule.query.get_or_404(id)
		request_dict = request.get_json(force=True)
		
		if 'description' in request_dict:
			schedule.description = request_dict['description']
		if 'start_date' in request_dict:
			schedule.start_date = request_dict['start_date']
		if 'end_date' in request_dict:
			schedule.end_date = request_dict['end_date']

		dumped_schedule, dump_errors = schedule_schema.dump(schedule)
		print(dumped_schedule)
		if dump_errors:
			print("dump errors")
			return dump_errors, status.HTTP_400_BAD_REQUEST
		validate_errors = schedule_schema.validate(dumped_schedule)
		if validate_errors:
			print("validate errors")
			return validate_errors, status.HTTP_400_BAD_REQUEST
		try:
			schedule.update()
			result = schedule_schema.dump(schedule).data
			return result, status.HTTP_200_OK
		except SQLAlchemyError as e:
			db.session.rollback()
			resp = {"error": str(e)}
			return resp, status.HTTP_400_BAD_REQUEST


class ScheduleListResource(AuthRequiredResource):
	def get(self):
		schedules = Schedule.query.all()
		result = schedule_schema.dump(schedules, many=True).data
		return result
	
	def post(self):
		request_dict = request.get_json()
		if not request_dict:
			response = {'error': 'No input data provided'}
			return response, status.HTTP_400_BAD_REQUEST
		errors = schedule_schema.validate(request_dict)
		if errors:
			return errors, status.HTTP_400_BAD_REQUEST
		try:
			description = request_dict['description']
			start_date = request_dict['start_date']
			end_date = request_dict['end_date']
			activity_id = request_dict['activity_id']
			schedule = Schedule(description=description, start_date=start_date, end_date=end_date, activity_id=activity_id)
			schedule.add(schedule)
			query = Schedule.query.get(schedule.id)
			result = schedule_schema.dump(query).data
			return result, status.HTTP_201_CREATED
			
		except SQLAlchemyError as e:
			db.session.rollback()
			response = {'error': str(e)}
			return response, status.HTTP_400_BAD_REQUEST