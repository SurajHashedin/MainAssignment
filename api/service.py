from .models import *
from rest_framework.response import Response
from django.core.serializers import serialize
from django.http import JsonResponse
import json

class TicketService:
    def __init__(self, request_type, request_json):

        self.request_type = request_type
        self.request_json = request_json 

    def dispach_to_function_call_method(self):
        """
        Dispatch method to appropriate function_call method based on request type
        """

        method = getattr(self, self.request_type,
                         lambda: "Invalid request_type")
        return method()

    def Get_a_list_of_Projects_and_related_issues(self):

        res = projects_table.objects.all().values()
        return Response({'data': str(list(res)), "Status_Message":"Success", "Status": 200})

    def Get_details_of_a_Project_by_title(self):
        project_title = json.loads(self.request_json)['project_title']
        res = projects_table.objects.filter(project_title=project_title)
        return Response({'data': str(list(res)), "Status_Message":"Success", "Status": 200})


    def Create_a_Project(self):
        data = json.loads(self.request_json)
        project_title = data['project_title']
        project_description = data['project_description']
        project_creator = data['project_creator'] 

        try:
            # creating row table with given data
            projects_table.objects.update_or_create(project_title= project_title, project_description= project_description, \
                project_creator= project_creator)
        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "Project is created", "Status_Message":"Success", "Status": 200}) 


    def Update_a_Project(self):

        data = json.loads(self.request_json)
        project_id = data['project_id']
        projecttable = projects_table.objects.filter(project_id=project_id)
        if 'project_title' in data:
            projecttable.update(project_title= data['project_title'])
        if 'project_description' in data:
            projecttable.update(project_description=data['project_description'])
        if 'project_creator' in data:
            projecttable.update(project_creator=data['project_creator'])

        return Response({"Message": "Project is updated", "Status_Message":"Success", "Status": 200})

    

    def Delete_a_Project(self):
        data = json.loads(self.request_json)
        project_id = data['project_id']
        projecttable = projects_table.objects.filter(project_id=project_id)

        try:
            projecttable.delete() 
        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "Project is deleted", "Status_Message":"Success", "Status": 200}) 

    def Get_a_list_of_Issues(self):

        res = issues_table.objects.all().values('issue_id', 'issue_title')
        return Response({'data': str(list(res)), "Status_Message":"Success", "Status": 200})

    def Get_details_of_an_Issue(self):

        res = issues_table.objects.filter().values()
        return Response({'data': str(list(res)), "Status_Message":"Success", "Status": 200})

    def Create_an_Issue(self):
        data = json.loads(self.request_json)
        issue_title = data['issue_title']
        issue_description = data['issue_description']
        issue_repoter = data['issue_repoter'] 
        issue_type = data['issue_type']
        issue_assignee = data['issue_assignee']
        issue_status = data['issue_status'] 
        project_title = data['project_title']

        try:
            # creating row table with given data
            issues_table.objects.create(issue_title= issue_title, issue_description= issue_description, \
                issue_repoter= issue_repoter, issue_type= issue_type, issue_assignee= issue_assignee,\
                    issue_status= issue_status, project_title=project_title)
        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "Issue is created", "Status_Message":"Success", "Status": 200}) 

    def Update_an_Issue(self):

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        issuetable = issues_table.objects.filter(issue_id=issue_id)
        if 'issue_title' in data:
            issuetable.update(issue_title= data['issue_title'])
        if 'issue_description' in data:
            issuetable.update(issue_description=data['issue_description'])
        if 'issue_repoter' in data:
            issuetable.update(issue_repoter=data['issue_repoter'])
        if 'issue_type' in data:
            issuetable.update(issue_type= data['issue_type'])
        if 'issue_assignee' in data:
            issuetable.update(issue_assignee=data['issue_assignee'])
        if 'issue_status' in data:
            issuetable.update(issue_status=data['issue_status'])
        if 'project_title' in data:
            issuetable.update(project_title=data['project_title'])          

        return Response({"Message": "Issue is updated", "Status_Message":"Success", "Status": 200})

    def Delete_an_Issue(self):
        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        issuetable = issues_table.objects.filter(issue_id=issue_id)
        try:
            issuetable.delete() 
        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "Issue is deleted", "Status_Message":"Success", "Status": 200})


    def Get_a_list_of_Issues_under_a_Project(self):
        data = json.loads(self.request_json)
        project_title = data['project_title']
        res = issues_table.objects.filter(project_title=project_title).values('issue_id', 'issue_title')
        return Response({'data': str(list(res)), "Status_Message":"Success", "Status": 200})

    def Get_details_of_an_Issue_under_a_Project(self):
        data = json.loads(self.request_json)
        project_title = data['project_title']
        res = issues_table.objects.filter(project_title=project_title).values()
        return Response({'data': str(list(res)), "Status_Message":"Success", "Status": 200})

    def Create_an_Issue_under_a_Project(self):
        data = json.loads(self.request_json)
        project_title = data['project_title']
        issue_title = data['issue_title']
        issue_description = data['issue_description']
        issue_repoter = data['issue_repoter'] 
        issue_type = data['issue_type']
        issue_assignee = data['issue_assignee']
        issue_status = data['issue_status'] 
        

        try:
            # creating row table with given data
            issues_table.objects.create(issue_title= issue_title, issue_description= issue_description, \
                issue_repoter= issue_repoter, issue_type= issue_type, issue_assignee= issue_assignee,\
                    issue_status= issue_status, project_title=project_title)
        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "Issue is created", "Status_Message":"Success", "Status": 200}) 

    def Update_an_Issue_under_a_Project(self):

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        project_title = data['project_title']
        issuetable = issues_table.objects.filter(issue_id=issue_id, project_title=project_title)
        if 'issue_title' in data:
            issuetable.update(issue_title= data['issue_title'])
        if 'issue_description' in data:
            issuetable.update(issue_description=data['issue_description'])
        if 'issue_repoter' in data:
            issuetable.update(issue_repoter=data['issue_repoter'])
        if 'issue_type' in data:
            issuetable.update(issue_type= data['issue_type'])
        if 'issue_assignee' in data:
            issuetable.update(issue_assignee=data['issue_assignee'])
        if 'issue_status' in data:
            issuetable.update(issue_status=data['issue_status'])
       

        return Response({"Message": "Issue is updated", "Status_Message":"Success", "Status": 200})


    def Delete_an_Issue_under_a_Project(self):
        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        project_title = data['project_title']

        issuetable = issues_table.objects.filter(issue_id=issue_id,project_title=project_title)
        try:
            issuetable.delete() 
        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "Issue is deleted", "Status_Message":"Success", "Status": 200})

    def Update_an_Issue_under_a_Project(self):

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        project_title = data['project_title']
        issuetable = issues_table.objects.filter(issue_id=issue_id, project_title=project_title)
        if 'issue_title' in data:
            issuetable.update(issue_title= data['issue_title'])
        if 'issue_description' in data:
            issuetable.update(issue_description=data['issue_description'])
        if 'issue_repoter' in data:
            issuetable.update(issue_repoter=data['issue_repoter'])
        if 'issue_type' in data:
            issuetable.update(issue_type= data['issue_type'])
        if 'issue_assignee' in data:
            issuetable.update(issue_assignee=data['issue_assignee'])
        if 'issue_status' in data:
            issuetable.update(issue_status=data['issue_status'])
       

        return Response({"Message": "Issue is updated", "Status_Message":"Success", "Status": 200})

    def Assign_an_Issue_to_a_User(self):

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        issuetable = issues_table.objects.filter(issue_id=issue_id)
        if 'issue_assignee' in data:
            issuetable.update(issue_assignee=data['issue_assignee'])

        return Response({"Message": "Issue is updated", "Status_Message":"Success", "Status": 200})

    def Update_the_Status_of_an_Issue(self):

        data = json.loads(self.request_json)
        issue_id = data['issue_id']

        issuetable = issues_table.objects.filter(issue_id=issue_id)
        if 'issue_status' in data:
            issuetable.update(issue_status=data['issue_status'])
       

        return Response({"Message": "Issue is updated", "Status_Message":"Success", "Status": 200})

    def Search_Issue_on_title_and_description(self):

        data = json.loads(self.request_json)
        issue_description = data['issue_description']
        issue_title = data['issue_title']

        res = issues_table.objects.filter(issue_description=issue_description, issue_title=issue_title).values()
       

        return Response({'data': str(list(res)), "Status_Message":"Success", "Status": 200})

    def Get_a_list_of_users(self):

        res = user.objects.filter().values()
        return Response({'data': str(list(res)), "Status_Message":"Success", "Status": 200})

