from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(Dept)
admin.site.register(Employe)
admin.site.register(Salgrade)
admin.site.register(Bonus)