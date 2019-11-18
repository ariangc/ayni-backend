from resources.security import AuthRequiredResource
from flask_restful import Resource
from flask import request, jsonify, make_response, g
import status

from controllers import projectCTL

class CreateProject(AuthRequiredResource):
	def post(self):
		d = request.get_json()
		if not d:
			response = {'user': 'No input data provided'}
			return response, status.HTTP_400_BAD_REQUEST

		organizationId = d['organizationId']
		name = d['name']
		imageDirection = d['imageDirection']
		
		return projectCTL.createProject(organizationId, name, imageDirection)

class DeleteProject(AuthRequiredResource):
	def post(self):
		d = request.get_json()
		if not d:
			response = {'user': 'No input data provided'}
			return response, status.HTTP_400_BAD_REQUEST
		projectId = d['projectId']
		return projectCTL.deleteProject(projectId)

class GetProjectXOrganization(AuthRequiredResource):
	def get(self):
		d = request.get_json()
		if not d:
			response = {'user': 'No input data provided'}
			return response, status.HTTP_400_BAD_REQUEST
		idOrganization = d['organizationId']
		return projectCTL.getProjectXOrganization(idOrganization), status.HTTP_200_OK

