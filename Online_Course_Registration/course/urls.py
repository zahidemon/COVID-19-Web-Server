from django.conf.urls import url
from course import views

app_name="course"

urlpatterns=[

    url(r'^$',views.OpenListView,name='open_list'),
    url(r'^later/',views.Later,name='later'),
    url(r'^confirm/',views.SendConfirm,name='confirm'),
    url(r'^addcourse/',views.AddCourse,name='addcourse'),
    url(r'^addoptionalcourse/',views.AddOptionalCourse,name='addoptionalcourse'),
    url(r'^registration/',views.RegView,name='registration'),
    url(r'^passed/',views.Passed,name='passed'),
    url(r'^search/',views.CourseSearch,name='coursesearch'),
    url(r'^searchlist/',views.Searchlist,name='searchlist'),
    url(r'^studentsearch/',views.StudentSearch,name='studentsearch'),
    url(r'^studentdelete/',views.StudentDelete,name='studentdelete'),
    url(r'^studentlist/',views.StudentList,name='studentlist'),
    url(r'^updatesemester/',views.UpdateSemester,name='updatesemester'),
    url(r'^regopen/',views.RegOpen,name='regopen'),
]
