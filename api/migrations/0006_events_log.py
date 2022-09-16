# Generated by Django 3.2.15 on 2022-09-16 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_events_logging'),
    ]

    operations = [
        migrations.CreateModel(
            name='events_log',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('request_type', models.CharField(choices=[('Get_a_list_of_Projects_and_related_issues', 'Get a list of Projects and related issues'), ('Get_details_of_a_Project_by_title', 'Get details of a Project by title'), ('Create_a_Project', 'Create a Project'), ('Update_a_Project', 'Update a Project'), ('Delete_a_Project', 'Delete a Project'), ('Get_a_list_of_Issues', 'Get a list of Issues'), ('Get_details_of_an_Issue', 'Get details of an Issue'), ('Create_an_Issue', 'Create an Issue'), ('Update_an_Issue', 'Update an Issue'), ('Delete_an_Issue', 'Delete an Issue'), ('Get_a_list_of_Issues_under_a_Project', 'Get a list of Issues under a Project'), ('Get_details_of_an_Issue_under_a_Project', 'Get details of an Issue under a Project'), ('Create_an_Issue_under_a_Project', 'Create an Issue under a Project'), ('Update_an_Issue_under_a_Project', 'Update an Issue under a Project'), ('Delete_an_Issue_under_a_Project', 'Delete an Issue under a Project'), ('Assign_an_Issue_to_a_User', 'Assign an Issue to a User'), ('Update_the_Status_of_an_Issue', 'Update the Status of an Issue'), ('Search_Issue_on_title_and_description', 'Search Issue on title and description'), ('Get_a_list_of_users', 'Get a list of users'), ('Add_a_label_to_the_issue', 'Add a label to the issue'), ('Delete_a_label_from_the_issue', 'Delete a label from the issue'), ('Add_a_Watcher_to_an_issue', 'Add a Watcher to an issue'), ('Delete_a_Watcher_from_the_issue', 'Delete a Watcher from the issue'), ('Create_a_Worklog_under_an_issue', 'Create a Worklog under an issue'), ('Update_the_worklog_as_described_above', 'Update the worklog as described above'), ('Delete_worklog_as_described_above', 'Delete worklog as described above'), ('Add_a_comment_under_an_issue', 'Add a comment under an issue'), ('Update_a_comment_as_described_above', 'Update a comment as described above'), ('Delete_a_comment_as_described_above', 'Delete a comment as described above')], max_length=300)),
                ('request_json', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'events_log',
            },
        ),
    ]
