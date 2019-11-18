import status
from app import db

from models.activity import Activity

def jsonify(act):
	d = {}
	d'id'] = act.id
	d'project_id'] = act.project_id
	d'title'] = act.title
	d'description'] = act.description
	d'latitude'] = act.latitude
	d'longitude'] = act.longitude
	return d

def createActivity(projectId, title, description, latitude, longitude):
	act = Activity(
		project_id = projectId, 
		title = title, 
		description = description, 
		latitude = latitude, 
		longitude = longitude
	) 
	return