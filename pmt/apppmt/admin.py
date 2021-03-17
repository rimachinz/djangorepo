from django.contrib import admin
from .models import manager,member,project,issues
admin.site.register(manager)
admin.site.register(member)
admin.site.register(project)
admin.site.register(issues)
