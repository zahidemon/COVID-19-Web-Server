from django.contrib import admin
from course.models import Courses,Open,Remind,Registration,Initial,OnlySemester,OptionalCourse

admin.site.register(Courses)
admin.site.register(Open)
admin.site.register(Remind)
admin.site.register(Registration)
admin.site.register(Initial)
admin.site.register(OnlySemester)
admin.site.register(OptionalCourse)
# Register your models here.
