from django.contrib import admin
from .models import Project, SoftSkill, Skill

admin.site.register([
    Project,
    SoftSkill,
    Skill
])