from resources.security import AuthRequiredResource
from flask_restful import Resource
from flask import request, jsonify, make_response, g
import status

from controllers import organizationCTL


class CreateOrganization(AuthRequiredResource):
    def post(self):
        d = request.get_json()
        if not d:
            response = {'user': 'No input data provided'}
            return response, status.HTTP_400_BAD_REQUEST
        userId = d['userId']
        listOfUsers = d['listOfUsers']
        name = d['name']
        telephone_number_1 = d['telephone1']
        telephone_number_2 = d['telephone2']
        email_1 = d['email1']
        email_2 = d['email2']
        direction = d['direction']
        image_direction = d['imageDirection']
        return organizationCTL.createOrganization(userId, listOfUsers, name, telephone_number_1, telephone_number_2, email_1, email_2, direction, image_direction)

class UpdateMembers(AuthRequiredResource):
    def post(self):
        d = request.get_json()
        if not d:
            response = {'user': 'No input data provided'}
            return response, status.HTTP_400_BAD_REQUEST
        organizationId = d['organizationId']
        listUsersIn = d['listUsersIn']
        listUsersOut = d['listUsersOut'] 
        return organizationCTL.updateMembers(organizationId, listUsersIn, listUsersOut)        

class GetOrganizationsXUser(AuthRequiredResource):
    def get(self):
        d = request.get_json()
        if not d:
            response = {'user': 'No input data provided'}
            return response, status.HTTP_400_BAD_REQUEST
        userId = d['userId']
        return organizationCTL.getOrganizationsXUser(userId)

class DeleteOrganization(AuthRequiredResource):
    def post(self):
        d = request.get_json()
        if not d:
            response = {'user': 'No input data provided'}
            return response, status.HTTP_400_BAD_REQUEST
        organizationId = d['organizationId']
        return organizationCTL.deleteOrganization(organizationId)
        