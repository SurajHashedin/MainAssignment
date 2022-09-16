from statistics import mode
from django.db import models
from .utils import Issue_Type, Status_Type
from datetime import datetime
# Create your models here.

class user(models.Model):
    """
    table to store user info
    """
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, null=False)
    user_email = models.CharField(max_length=100, null=False)
    user_password = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return str(self.user_name)

    class Meta:
        db_table = 'user'


class projects_table(models.Model):
    """
    create projects table to main all information related projects
    """
    project_id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=100, null=False)
    project_description = models.CharField(max_length=500, null=False)
    project_creator = models.CharField(max_length=100, null=False)

    def __str__(self):
        return str(self.project_id)+'-'+str(self.project_title)+'-'+str(self.project_description)+'-'+str(self.project_creator)

    class Meta:
        db_table = 'projects_table'

#created tuple for status choice
_STATUS_CHOICES = [
    ('Open', 'Open'),
    ("InProgress", 'InProgress'),
    ("InReview", 'In Review'),
    ("CodeComplete", 'Code Complete'),
    ('Done', 'Done')
]

#created tuple for issue choice
_ISSUE_CHOICES = [
    ('BUG', 'BUG'),
    ("TASK", 'TASK'),
    ("STORY", 'STORY'),
    ("EPIC", 'EPIC')
]

#created tuple for request choice
_REQUEST_TYPE_CHOICES = [
    ('Get_a_list_of_Projects_and_related_issues', 'Get a list of Projects and related issues'),
    ('Get_details_of_a_Project_by_title', 'Get details of a Project by title'),
    ('Create_a_Project', 'Create a Project'),
    ('Update_a_Project', 'Update a Project'),
    ('Delete_a_Project', 'Delete a Project'),
    ('Get_a_list_of_Issues', 'Get a list of Issues'),
    ('Get_details_of_an_Issue', 'Get details of an Issue'),
    ('Create_an_Issue', 'Create an Issue'),
    ('Update_an_Issue', 'Update an Issue'),
    ('Delete_an_Issue', 'Delete an Issue'),
    ('Get_a_list_of_Issues_under_a_Project', 'Get a list of Issues under a Project'),
    ('Get_details_of_an_Issue_under_a_Project', 'Get details of an Issue under a Project'),
    ('Create_an_Issue_under_a_Project', 'Create an Issue under a Project'),
    ('Update_an_Issue_under_a_Project', 'Update an Issue under a Project'),
    ('Delete_an_Issue_under_a_Project', 'Delete an Issue under a Project'),
    ('Assign_an_Issue_to_a_User', 'Assign an Issue to a User'),
    ('Update_the_Status_of_an_Issue', 'Update the Status of an Issue'),
    ('Search_Issue_on_title_and_description', 'Search Issue on title and description'),
    ('Get_a_list_of_users', 'Get a list of users'),
    ('Add_a_label_to_the_issue', 'Add a label to the issue'),
    ('Delete_a_label_from_the_issue', 'Delete a label from the issue'),
    ('Add_a_Watcher_to_an_issue', 'Add a Watcher to an issue'),
    ('Delete_a_Watcher_from_the_issue', 'Delete a Watcher from the issue'),
    ('Create_a_Worklog_under_an_issue', 'Create a Worklog under an issue'),
    ('Update_the_worklog_as_described_above', 'Update the worklog as described above'),
    ('Delete_worklog_as_described_above', 'Delete worklog as described above'),
    ('Add_a_comment_under_an_issue', 'Add a comment under an issue'),
    ('Update_a_comment_as_described_above', 'Update a comment as described above'),
    ('Delete_a_comment_as_described_above', 'Delete a comment as described above')
]

class events_log(models.Model):
    """
    logging all request in event log table
    """
    request_id = models.AutoField(primary_key=True)
    request_type = models.CharField(
        max_length=300, choices=_REQUEST_TYPE_CHOICES)
    request_json = models.CharField(max_length=10000, null=False)
    def __str__(self):
        return str(self.request_id)+'-'+str(self.request_type)

    class Meta:
        db_table = 'events_log'

#table to create new issue
class issues_table(models.Model):
    """
    maintaing status of issue and issue type and other fields
    """
    issue_id = models.AutoField(primary_key=True)
    issue_title = models.CharField(max_length=100, null=False)
    issue_description = models.CharField(max_length=100, null=False)
    issue_repoter = models.CharField(max_length=100, null=False)
    issue_type = models.CharField(
        max_length=100, choices=_ISSUE_CHOICES, default='TASK')
    issue_assignee = models.CharField(max_length=100, null=False)
    issue_status = models.CharField(
        max_length=100, choices=_STATUS_CHOICES, default='Open')
    project_title = models.CharField(max_length=100, null=False)
    assignlabel = models.CharField(max_length=100, null=False,default=None)
    creation_time = models.DateTimeField(null=True, blank=True, default=datetime.now)
    time_allocated_in_day = models.IntegerField(null=False,default=None)
    comments = models.CharField(max_length=500, null=False,default=None)
    watchers = models.CharField(max_length=500, null=False, default=None)


    def __str__(self):
        return str(self.issue_id)+'-'+str(self.issue_title)+'-'+str(self.issue_description)+'-'+str(self.issue_repoter)+'-'+\
            str(self.issue_type)+'-'+str(self.issue_assignee)+'-'+str(self.issue_status)+'-'+str(self.project_title)+'-'+str(\
            self.assignlabel)+'-'+str(self.creation_time)+'-'+str(self.time_allocated_in_day)+'-'+str(self.comments)+(self.watchers)

    class Meta:
        db_table = 'issues_table'

class ticket_requests(models.Model):
    """
    logging all request in ticket request table
    """
    request_id = models.AutoField(primary_key=True)
    request_type = models.CharField(
        max_length=300, choices=_REQUEST_TYPE_CHOICES)
    request_json = models.CharField(max_length=100, null=False)
    def __str__(self):
        return str(self.request_id)+'-'+str(self.request_type)

    class Meta:
        db_table = 'ticket_requests'

class events_logging(models.Model):
    """
    logging all request in event logging table
    """
    request_id = models.AutoField(primary_key=True)
    request_type = models.CharField(
        max_length=300, choices=_REQUEST_TYPE_CHOICES)
    request_json = models.CharField(max_length=100, null=False)
    def __str__(self):
        return str(self.request_id)

    class Meta:
        db_table = 'events_logging'