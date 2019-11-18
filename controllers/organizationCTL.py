import status
from app import db

from models.organization import Organization
from models.user_x_organization import User_x_Organization

def jsonifyOrganization(obj):
	d = {}
	d['id'] = obj.id
	d['name'] = obj.name
	d['created_date'] = obj.created_date.__str__()
	d['telephone_number_1'] = obj.telephone_number_1
	d['telephone_number_2'] = obj.telephone_number_2
	d['email_1'] = obj.email_1
	d['email_2'] = obj.email_2
	d['direction'] = obj.direction
	d['flg_active'] = obj.flg_active
	d['image_direction'] = obj.image_direction
	d['id_creator'] = obj.id_creator
	d['reference_1'] = obj.reference_1
	return d

def addMemberOrganization(userId, organizationId):
	obj = User_x_Organization(
		organization_id = organizationId,
		user_id = userId
	)
	obj = User_x_Organization.addOne(obj)
	return 1

def createOrganization(userId, listOfUsers, name, telephone_number_1, telephone_number_2, email_1, email_2, direction, image_direction, reference1):
	org = Organization(
		name = name,
		telephone_number_1 = telephone_number_1,
		telephone_number_2 = telephone_number_2,
		email_1 = email_1,
		email_2 = email_2,
		direction = direction,
		image_direction = image_direction,
		id_creator = userId,
		reference_1 = reference1
	)
	idOrg = Organization.addOne(org)
	addMemberOrganization(userId, idOrg)
	for i in listOfUsers:
		addMemberOrganization(i, idOrg)
	return {"organizationId": idOrg}, status.HTTP_200_OK

def updateMembers(organizationId, listUsersIn, listUsersOut):
	for i in listUsersIn:
		exists, isActive = User_x_Organization.verifyExistActive(organizationId, i)
		if not exists:
			addMemberOrganization(i, organizationId)
		if exists and not isActive:
			User_x_Organization.turnFlg(organizationId, i)
	for j in listUsersOut:
		exists, isActive = User_x_Organization.verifyExistActive(i, organizationId)
		if exists and isActive:
			User_x_Organization.turnFlg(organizationId, j)
	return status.HTTP_200_OK

def getOrganizationsXUser(userId):
	subOne = db.session.query(User_x_Organization).filter(User_x_Organization.user_id == userId, User_x_Organization.flg_active == 1).subquery()
	subTwo = db.session.query(Organization).join(subOne, subOne.c.organization_id == Organization.id).all()
	d = {}
	list = []
	for i in subTwo:
		list.append(jsonifyOrganization(i))
	d['listOfOrganizations'] = list
	return d, status.HTTP_200_OK

def deleteOrganization(organizationId):
	Organization.turnFlg(organizationId)
	listUsers = User_x_Organization.query.filter(User_x_Organization.organization_id == organizationId, User_x_Organization.flg_active == 1).all()
	for i in listUsers:
		User_x_Organization.turnFlg(organizationId, i.user_id)
	return status.HTTP_200_OK
