from django.contrib import admin
from .models import Courses, Notions, GearRequirements, EnrollingRequirements

# Register your models here.

admin.site.register(Courses)
admin.site.register(Notions)
admin.site.register(GearRequirements)
admin.site.register(EnrollingRequirements)

