from models.project import Project
import status
from app import db

def jsonify(project):
    d = {}
    d['id'] = project.id
    d['organization_id'] = project.organization_id
    d['name'] = project.name
    d['created_date'] = project.created_date.__str__()
    d['flg_active'] = project.flg_active
    d['image_direction'] = project.image_direction
    return d

def createProject(organizationId, name, imageDirection):
    pro = Project(
        organization_id = organizationId,
        name = name,
        image_direction = imageDirection
    )
    idProject = Project.addOne(pro)

    return {"projectId": idProject}, status.HTTP_200_OK

def deleteProject(projectId):
    Project.turnFlg(projectId)
    return status.HTTP_200_OK

def getProjectXOrganization(idOrganization):
    subOne = Project.query.filter(Project.organization_id == idOrganization, Project.flg_active == 1).all()
    d = {}
    list = []
    for i in subOne:
        list.append(jsonify(i))
    d['listOfProjects'] = list
    return d