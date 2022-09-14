from django.contrib import admin
from .models import (projects_table, issues_table, user,)
# Register your models here.


admin.site.register((projects_table, issues_table, user,))