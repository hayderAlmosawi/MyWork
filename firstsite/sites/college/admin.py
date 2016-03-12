from django.contrib import admin

# Register your models here.

from .models import Marks,Subject,Department,Student,Specilization,ScientificResearch,Teacher,Teacher_Subject

admin.site.register(Marks)
admin.site.register(Subject)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Specilization)
admin.site.register(ScientificResearch)
admin.site.register(Teacher)
admin.site.register(Teacher_Subject)

