from django.contrib import admin
from .models import Project
# Register your models here.
admin.site.register(Project)
admin.site.site_header = "Admin Dashboard"
admin.site.site_title = "Dashboard"
admin.site.index_title = "Welcome To Admin Dashboard."