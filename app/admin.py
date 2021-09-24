from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(NewsDetails)
admin.site.register(Site)
admin.site.register(NewsComment)