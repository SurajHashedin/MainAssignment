from statistics import mode
from django.db import models
from .utils import Issue_Type, Status_Type
# Create your models here.

class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, null=False)
    user_email = models.CharField(max_length=100, null=False)
    user_password = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return str(self.user_id)

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

#table to create new issue
class issues_table(models.Model):
    """
    maintaing status of issue and issue type
    """
    issue_id = models.AutoField(primary_key=True)
    issue_title = models.CharField(max_length=100, null=False)
    issue_description = models.CharField(max_length=100, null=False)

    # issue_repoter = models.ForeignKey(                 /// take usename from authentication
    #     user, on_delete=models.SET_NULL, max_length=100, null=True, db_column='issue_repoter_user_id', related_name='issue_repoter_user_id')

    # issue_repoter = models.CharField(max_length=100, null=False)
    issue_type = models.CharField(
        max_length=100, choices=_ISSUE_CHOICES, default='TASK')
    issue_assignee = models.ForeignKey(
        user, on_delete=models.SET_NULL, max_length=100, null=True, db_column='issue_assignee_user_id', related_name='issue_assignee_user_id')
    issue_status = models.CharField(
        max_length=100, choices=_STATUS_CHOICES, default='Open')
    project_name = models.ForeignKey(
        projects_table, on_delete=models.CASCADE, max_length=100, null=False, db_column='project_name', related_name='projects_table_project_name')


    def __str__(self):
        return str(self.issue_title)

    class Meta:
        db_table = 'issues_table'

