from statistics import mode
from django.db import models
from .utils import Issue_Type, Status_Type
from datetime import datetime
# Create your models here.

class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, null=False)
    user_email = models.CharField(max_length=100, null=False)
    user_password = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return str(self.user_name)

    class Meta:
        db_table = 'user'

#create projects table to main all information related projects
class projects_table(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=100, null=False)
    project_description = models.CharField(max_length=500, null=False)
    project_creator = models.CharField(max_length=100, null=False)
    # user_id = models.ForeignKey(
    #     user, on_delete=models.CASCADE, max_length=100, null=False, db_column='user_id', related_name='user_user_id')
    # project_user_name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return str(self.project_title)

    class Meta:
        db_table = 'projects_table'

_STATUS_CHOICES = [
    ('Open', 'Open'),
    ("InProgress", 'InProgress'),
    ("InReview", 'In Review'),
    ("CodeComplete", 'Code Complete'),
    ('Done', 'Done')
]

_ISSUE_CHOICES = [
    ('BUG', 'BUG'),
    ("TASK", 'TASK'),
    ("STORY", 'STORY'),
    ("EPIC", 'EPIC')
]

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
    ('Get_a_list_of_users', 'Get a list of users')
]

class ticket_requests(models.Model):

    request_id = models.AutoField(primary_key=True)
    request_type = models.CharField(
        max_length=300, choices=_REQUEST_TYPE_CHOICES)
    request_json = models.CharField(max_length=100, null=False)
    def __str__(self):
        return str(self.request_id, self.request_type)

    class Meta:
        db_table = 'ticket_requests'
#table to create new issue
class issues_table(models.Model):
    """
    maintaing status of issue and issue type
    """
    issue_id = models.AutoField(primary_key=True)
    issue_title = models.CharField(max_length=100, null=False)
    issue_description = models.CharField(max_length=100, null=False)
    # issue_repoter = models.ForeignKey(                 # take usename from authentication
    #     user, on_delete=models.SET_NULL, max_length=100, null=True, db_column='user_id', related_name='issue_repoter_user_id')
    issue_repoter = models.CharField(max_length=100, null=False)
    issue_type = models.CharField(
        max_length=100, choices=_ISSUE_CHOICES, default='TASK')
    issue_assignee = models.CharField(max_length=100, null=False)
    issue_status = models.CharField(
        max_length=100, choices=_STATUS_CHOICES, default='Open')
    project_title = models.CharField(max_length=100, null=False)
        #projects_table, on_delete=models.SET_NULL , max_length=100, null=True) #, db_column='project_title', related_name='projects_table_project_title')
    label = models.CharField(max_length=100, null=False)
    creation_time = models.DateTimeField(null=True, blank=True, default=datetime.now)
    time_allocated_in_day = models.IntegerField(null=False)
    comments = models.CharField(max_length=500, null=False)
    def __str__(self):
        return str(self.issue_title)

    class Meta:
        db_table = 'issues_table'

