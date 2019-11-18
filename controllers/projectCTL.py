from models.project import Project
import status
from app import db

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

