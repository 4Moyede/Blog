from django.contrib import admin

# Register your models here.
from portfolio.models import Introduce, Experience, Skill

admin.site.register(Introduce)
admin.site.register(Experience)
admin.site.register(Skill)