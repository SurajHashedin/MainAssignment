from django.contrib import admin
from .models import (projects_table, issues_table, user, events_log,)
# Register your models here.


admin.site.register((projects_table, issues_table, user, events_log,))