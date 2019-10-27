from models.news import News, NewsSchema
from flask import request
from resources.security import AuthRequiredResource
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError
from app import db
import status

news_schema = NewsSchema()

class NewsResource(AuthRequiredResource):
	def get(self, id):
		news = News.query.get_or_404(id)
		result = news_schema.dump(news).data
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
			result = schedule_schema.dump(activity).data
			return result, status.HTTP_200_OK
		except SQLAlchemyError as e:
			db.session.rollback()
			resp = {"error": str(e)}
			return resp, status.HTTP_400_BAD_REQUEST

class NewsListResource(AuthRequiredResource):
	def get(self):
		news = News.query.all()
		result = news_schema.dump(news, many=True).data
		return result
	
	def post(self):
		request_dict = request.get_json()
		if not request_dict:
			response = {'error': 'No input data provided'}
			return response, status.HTTP_400_BAD_REQUEST
		errors = news_schema.validate(request_dict)
		if errors:
			return errors, status.HTTP_400_BAD_REQUEST
		try:
			title = request_dict['title']
			description = request_dict['description']
			activity_id = request_dict['activity_id']
			news = News(title=title, description=description, activity_id=activity_id)
			news.add(news)
			query = News.query.get(news.id)
			result = news_schema.dump(query).data
			return result, status.HTTP_201_CREATED
			
		except SQLAlchemyError as e:
			db.session.rollback()
			response = {'error': str(e)}
			return response, status.HTTP_400_BAD_REQUEST
		
