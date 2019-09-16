from controllers import likeCTL
from resources.security import AuthRequiredResource
from models.like import LikeSchema
from flask_restful import Resource
from flask import request, jsonify, make_response, g
import status

like_schema = LikeSchema()

class AddLikeResource(AuthRequiredResource):
	def post(self):
		d = request.get_json()
		if not d:
			response = {'user': 'No input data provided'}
			return response, status.HTTP_400_BAD_REQUEST
		
		name = d["name"]
		description = d["description"]
		logodir = d["logodir"]

		errors = like_schema.validate({"name": name, "description": description})
		if errors:
			return errors, status.HTTP_400_BAD_REQUEST
		
		return likeCTL.addLike(name, description, logodir)



		