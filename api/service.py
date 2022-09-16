from .models import *
from rest_framework.response import Response
from django.core.serializers import serialize
from django.http import JsonResponse
import json
import logging


#creating object to take log on server
logger = logging.getLogger(__name__)

class TicketService:
    """
    class which recieve all request type of StarkIndustries
    """
    def __init__(self, request_type, request_json):

        self.request_type = request_type
        self.request_json = request_json 

    def dispach_to_function_call_method(self):
        """
        Dispatch method to appropriate function_call method based on request type
        """
        logger.debug('request is dispatch respective method')
        method = getattr(self, self.request_type,
                         lambda: "Invalid request_type")
                
        return method()

    def Get_a_list_of_Projects_and_related_issues(self):
        """
        method to accept Get_a_list_of_Projects_and_related_issues request
        """
        logger.debug('request is processing')
        res = projects_table.objects.all().values()
        return Response({'data': str(list(res)), "Status_Message":"Success", "Status": 200})

    def Get_details_of_a_Project_by_title(self):
        """
        method to accept Get_details_of_a_Project_by_title request
        """

        project_title = json.loads(self.request_json)['project_title']
        res = projects_table.objects.filter(project_title=project_title)
        return Response({'data': str(list(res)), "Status_Message":"Success", "Status": 200})


    def Create_a_Project(self):
        """
        method to accept Create_a_Project request
        """

        data = json.loads(self.request_json)
        project_title = data['project_title'] if 'project_title' in data else ''
        project_description = data['project_description'] if 'project_description' in data else ''
        project_creator = data['project_creator'] if 'project_creator' in data else ''
        logger.debug('request is processing')
        try:
            # creating row table with given data
            projects_table.objects.update_or_create(project_title= project_title, project_description= project_description, \
                project_creator= project_creator)
        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "Project is created", "Status_Message":"Success", "Status": 200}) 


    def Update_a_Project(self):
        """
        method to accept Update_a_Project request
        """

        data = json.loads(self.request_json)
        project_id = data['project_id']
        projecttable = projects_table.objects.filter(project_id=project_id)

        logger.debug('request is processing')

        if 'project_title' in data:
            projecttable.update(project_title= data['project_title'])
        if 'project_description' in data:
            projecttable.update(project_description=data['project_description'])
        if 'project_creator' in data:
            projecttable.update(project_creator=data['project_creator'])

        return Response({"Message": "Project is updated", "Status_Message":"Success", "Status": 200})

    

    def Delete_a_Project(self):
        """
        method to accept Delete_a_Project request
        """

        data = json.loads(self.request_json)
        project_id = data['project_id']
        projecttable = projects_table.objects.filter(project_id=project_id)

        logger.debug('request is processing')

        try:
            projecttable.delete() 
        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "Project is deleted", "Status_Message":"Success", "Status": 200}) 

    def Get_a_list_of_Issues(self):
        """
        method to accept Get_a_list_of_Issues request
        """
        logger.debug('request is processing')

        res = issues_table.objects.all().values('issue_id', 'issue_title')
        return Response({'data': str(list(res)), "Status_Message":"Success", "Status": 200})

    def Get_details_of_an_Issue(self):
        """
        method to accept Get_details_of_an_Issue request
        """
        logger.debug('request is processing')
        res = issues_table.objects.filter().values()
        return Response({'data': str(list(res)), "Status_Message":"Success", "Status": 200})

    def Create_an_Issue(self):
        """
        method to accept Create_an_Issue request
        """

        data = json.loads(self.request_json)
        issue_title = data['issue_title'] if 'issue_title' in data else ''
        issue_description = data['issue_description'] if 'issue_description' in data else ''
        issue_repoter = data['issue_repoter'] if 'issue_repoter' in data else ''
        issue_type = data['issue_type'] if 'issue_type' in data else ''
        issue_assignee = data['issue_assignee'] if 'issue_assignee' in data else ''
        issue_status = data['issue_status'] if 'issue_status' in data else ''
        project_title = data['project_title'] if 'project_title' in data else ''
        assignlabel = data['assignlabel'] if 'assignlabel' in data else ''
        time_allocated_in_day = data['time_allocated_in_day'] if 'time_allocated_in_day' in data else ''
        comments = data['comments'] if 'comments' in data else ''
        watchers = data['watchers'] if 'watchers' in data else ''

        logger.debug('request is processing')
        try:
            # creating row table with given data
            issues_table.objects.create(issue_title= issue_title, issue_description= issue_description, \
                issue_repoter= issue_repoter, issue_type= issue_type, issue_assignee= issue_assignee,\
                    issue_status= issue_status, project_title=project_title,assignlabel=assignlabel,\
                        time_allocated_in_day=time_allocated_in_day,  comments=comments, watchers=watchers)
        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "Issue is created", "Status_Message":"Success", "Status": 200}) 

    def Update_an_Issue(self):
        """
        method to accept Update_an_Issue request
        """

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        issuetable = issues_table.objects.filter(issue_id=issue_id)

        logger.debug('request is processing')

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
        """
        method to accept Delete_an_Issue request
        """

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        issuetable = issues_table.objects.filter(issue_id=issue_id)
        logger.debug('request is processing')
        try:
            issuetable.delete() 
        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "Issue is deleted", "Status_Message":"Success", "Status": 200})


    def Get_a_list_of_Issues_under_a_Project(self):
        """
        method to accept Get_a_list_of_Issues_under_a_Project request
        """

        data = json.loads(self.request_json)
        project_title = data['project_title']
        logger.debug('request is processing')

        res = issues_table.objects.filter(project_title=project_title).values('issue_id', 'issue_title')
        return Response({'data': str(list(res)), "Status_Message":"Success", "Status": 200})

    def Get_details_of_an_Issue_under_a_Project(self):
        """
        method to accept Get_details_of_an_Issue_under_a_Project request
        """

        data = json.loads(self.request_json)
        project_title = data['project_title']
        logger.debug('request is processing')

        res = issues_table.objects.filter(project_title=project_title).values()
        return Response({'data': str(list(res)), "Status_Message":"Success", "Status": 200})

    def Create_an_Issue_under_a_Project(self):
        """
        method to accept Create_an_Issue_under_a_Project request
        """

        data = json.loads(self.request_json)
        project_title = data['project_title'] if 'project_title' in data else ''
        issue_title = data['issue_title'] if 'issue_title' in data else ''
        issue_description = data['issue_description'] if 'issue_description' in data else ''
        issue_repoter = data['issue_repoter'] if 'issue_repoter' in data else ''
        issue_type = data['issue_type'] if 'issue_type' in data else ''
        issue_assignee = data['issue_assignee'] if 'issue_assignee' in data else ''
        issue_status = data['issue_status'] if 'issue_status' in data else ''
        logger.debug('request is processing')

        try:
            # creating row table with given data
            issues_table.objects.create(issue_title= issue_title, issue_description= issue_description, \
                issue_repoter= issue_repoter, issue_type= issue_type, issue_assignee= issue_assignee,\
                    issue_status= issue_status, project_title=project_title)
        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "Issue is created", "Status_Message":"Success", "Status": 200}) 

    def Update_an_Issue_under_a_Project(self):
        """
        method to accept Update_an_Issue_under_a_Project request
        """

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        project_title = data['project_title']
        logger.debug('request is processing')
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
        """
        method to accept Delete_an_Issue_under_a_Project request
        """

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        project_title = data['project_title']
        logger.debug('request is processing')

        issuetable = issues_table.objects.filter(issue_id=issue_id,project_title=project_title)
        try:
            issuetable.delete() 
        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "Issue is deleted", "Status_Message":"Success", "Status": 200})

    def Update_an_Issue_under_a_Project(self):
        """
        method to accept Update_an_Issue_under_a_Project request
        """

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        project_title = data['project_title']
        logger.debug('request is processing')

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
        """
        method to accept Assign_an_Issue_to_a_User request
        """

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        logger.debug('request is processing')

        issuetable = issues_table.objects.filter(issue_id=issue_id)
        if 'issue_assignee' in data:
            issuetable.update(issue_assignee=data['issue_assignee'])

        return Response({"Message": "Issue is updated", "Status_Message":"Success", "Status": 200})

    def Update_the_Status_of_an_Issue(self):
        """
        method to accept Update_the_Status_of_an_Issue request
        """

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        logger.debug('request is processing')

        issuetable = issues_table.objects.filter(issue_id=issue_id)
        if 'issue_status' in data:
            issuetable.update(issue_status=data['issue_status'])
       

        return Response({"Message": "Issue is updated", "Status_Message":"Success", "Status": 200})

    def Search_Issue_on_title_and_description(self):
        """
        method to accept Search_Issue_on_title_and_description request
        """

        data = json.loads(self.request_json)
        issue_description = data['issue_description']
        issue_title = data['issue_title']

        logger.debug('request is processing')

        res = issues_table.objects.filter(issue_description=issue_description, issue_title=issue_title).values()
        return Response({'data': str(list(res)), "Status_Message":"Success", "Status": 200})

    def Get_a_list_of_users(self):
        """
        method to accept Get_a_list_of_users request
        """

        logger.debug('request is processing')
        res = user.objects.filter().values()
        return Response({'data': str(list(res)), "Status_Message":"Success", "Status": 200})


    def Add_a_label_to_the_issue(self):
        """
        method to accept Add_a_label_to_the_issue request
        """

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        logger.debug('request is processing')

        issuetable = issues_table.objects.filter(issue_id=issue_id)
        if 'assignlabel' in data:
            issuetable.update(assignlabel=data['assignlabel'])

        return Response({"Message": "Added a label to the issue", "Status_Message":"Success", "Status": 200})

    def Delete_a_label_from_the_issue(self):
        """
        method to accept Delete_a_label_from_the_issue request
        """

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        logger.debug('request is processing')

        issuetable = issues_table.objects.filter(issue_id=issue_id)
        try:
            issuetable.delete()

        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "Delete_a_label_from_the_issued", "Status_Message":"Success", "Status": 200})

    def Add_a_Watcher_to_an_issue(self):
        """
        method to accept Add_a_Watcher_to_an_issue request
        """

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        logger.debug('request is processing')

        issuetable = issues_table.objects.filter(issue_id=issue_id)
        if 'watchers' in data:
            issuetable.update(watchers=data['watchers'])

        return Response({"Message": "Add_a_Watcher_to_an_issue", "Status_Message":"Success", "Status": 200})

    def Delete_a_Watcher_from_the_issue(self):
        """
        method to accept Delete_a_Watcher_from_the_issue request
        """

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        watchers = data['watchers']
        logger.debug('request is processing')

        issuetable = issues_table.objects.filter(issue_id=issue_id, watchers=watchers)
        try:
            issuetable.delete()

        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "Delete_a_Watcher_from_the_issue", "Status_Message":"Success", "Status": 200})

    def Create_a_Worklog_under_an_issue(self):
        """
        method to accept Create_a_Worklog_under_an_issue request
        """

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        logger.debug('request is processing')

        issuetable = issues_table.objects.filter(issue_id=issue_id)
        if 'time_allocated_in_day' in data:
            issuetable.update(time_allocated_in_day=data['time_allocated_in_day'])

        return Response({"Message": "Create_a_Worklog_under_an_issue", "Status_Message":"Success", "Status": 200})

    def Update_the_worklog_as_described_above(self):
        """
        method to accept Update_the_worklog_as_described_above request
        """

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        logger.debug('request is processing')

        issuetable = issues_table.objects.filter(issue_id=issue_id)
        if 'time_allocated_in_day' in data:
            issuetable.update(time_allocated_in_day=data['time_allocated_in_day'])

        return Response({"Message": "Update_the_worklog_as_described_above", "Status_Message":"Success", "Status": 200})


    def Delete_worklog_as_described_above(self):
        """
        method to accept Delete_worklog_as_described_above request
        """

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        time_allocated_in_day = data['time_allocated_in_day']
        logger.debug('request is processing')

        issuetable = issues_table.objects.filter(issue_id=issue_id,time_allocated_in_day=time_allocated_in_day)
        try:
            issuetable.delete()

        except Exception as e:
            return Response({"Message": str(e), "Status_Message":"Failed", "Status": 400}) 

        return Response({"Message": "Delete_worklog_as_described_above", "Status_Message":"Success", "Status": 200})


    def Update_a_comment_as_described_above(self):
        """
        method to accept Update_a_comment_as_described_above request
        """

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        logger.debug('request is processing')

        issuetable = issues_table.objects.filter(issue_id=issue_id)
        if 'comments' in data:
            issuetable.update(comments=data['comments'])

        return Response({"Message": "Update_a_comment_as_described_above", "Status_Message":"Success", "Status": 200})

    def Delete_a_comment_as_described_above(self):
        """
        method to accept Delete_a_comment_as_described_above request
        """

        data = json.loads(self.request_json)
        issue_id = data['issue_id']
        comments = data['comments']
        logger.debug('request is processing')

        issuetable = issues_table.objects.filter(issue_id=issue_id,comments=comments)
        try:
            issuetable.delete()

        except Exception as e:
            return Response({"Message": 'Delete_a_comment_as_described_above', "Status_Message":"Failed", "Status": 400}) 