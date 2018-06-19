from django.shortcuts import render,get_object_or_404, redirect
from course.models import Courses,Open,Remind,Registration,Initial,OnlySemester,OptionalCourse
from course.forms import RemindForm,RegistrationForm,InitialForm,SearchForm,CoursesForm,Deleteform,OpenForm,OptionalCourseForm
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from datetime import date
import time
from django.contrib.auth.decorators import login_required


def OpenListView(request):
    model= Open
    form_class= InitialForm
    form=form_class(request.POST)
    c=Open.objects.filter(finish_date__gte=date.today())

    if request.method=='POST':

        if form.is_valid():
            form.save(commit=True)
        x= form.cleaned_data['Semester']
        y= Open.objects.filter(semester=x,finish_date__gte=date.today())
        if not y:
            return redirect('course:passed')
        else:
            return redirect('course:registration')
    else:
        form= InitialForm()


    return render(request,'course/open_list.html',{'form':form,'c':c})


def RegView(request):
    form_class= RegistrationForm
    form=form_class(request.POST)
    x= Initial.objects.filter().order_by('-id')[0]
    z=  Initial.objects.filter().order_by('-id')[1]
    print(x,z)
    my_dict={'x':x,'z':z}
    print(my_dict["x"].Department)
    print(my_dict["x"].Semester)
    y= Courses.objects.filter(Department=my_dict["x"].Department,Semester=my_dict["x"].Semester)
    p= OptionalCourse.objects.filter(Department=my_dict["x"].Department,Semester=my_dict["x"].Semester,Type="Optional I")
    q= OptionalCourse.objects.filter(Department=my_dict["x"].Department,Semester=my_dict["x"].Semester,Type="Optional II")

    if request.method=='POST':

        if form.is_valid():
            form.save(commit=True)
            s=""
            for e in y:
                s=s+e.Course_id
                s=s+" ,"
            var1 = request.POST.getlist('course1')

            for v in var1:
                s=s+v
                s=s+" ,"
            var2 = request.POST.getlist('course2')

            for v in var2:
                s=s+v
                s=s+" ,"
            print(s)
            Registration.objects.filter(Roll=form.cleaned_data["Roll"]).update(Courses=s)
        return redirect('course:open_list')
    else:
        form= RegistrationForm()
    return render(request,'course/courses_list.html',{'form':form,'y':y,'x':x,'p':p,'q':q})

def Later(request):
    form_class= RemindForm
    form=form_class(request.POST)
    if request.method=='POST':

        if form.is_valid():
            form.save(commit=True)

            msg = EmailMessage('Reminder',
                       'Your Course Registrtion will be ended soon.Register your courses as soon as possible', to=[form.cleaned_data['Email']])
            msg.send()
            return redirect('course:confirm')
    else:
        form= RemindForm()
    return render(request,'course/later_form.html',{'form':form})

def SendConfirm(request):
    obj= Remind.objects.filter().order_by('-id')[0]
    my_dict={'insert_me': obj.Email}
    return render(request,'course/confirm.html',context=my_dict)

def signout(request):
    logout(request)
    return redirect('course:open_list')

def Passed(request):
    return render(request,'course/passed.html')

def Searchlist(request):
    x= Initial.objects.filter().order_by('-id')[0]
    z=  Initial.objects.filter().order_by('-id')[1]
    print(x,z)
    my_dict={'x':x,'z':z}
    print(my_dict["x"].Department)
    print(my_dict["x"].Semester)
    sem=my_dict["x"].Semester
    dep=my_dict["x"].Department
    p= OptionalCourse.objects.filter(Department=my_dict["x"].Department,Semester=my_dict["x"].Semester,Type="Optional I")
    q= OptionalCourse.objects.filter(Department=my_dict["x"].Department,Semester=my_dict["x"].Semester,Type="Optional II")
    y= Courses.objects.filter(Department=my_dict["x"].Department,Semester=my_dict["x"].Semester)
    return render(request,'course/searchlist.html',{'y':y,'sem':sem,'dep':dep,'p':p,'q':q})

def CourseSearch(request):
    form_class= SearchForm
    form1=form_class(request.POST)

    if request.method=='POST':

        if form1.is_valid():
            form1.save(commit=True)
            return redirect('course:searchlist')


    else:
        form1= InitialForm()
    return render(request,'course/course_search.html',{'form1':form1})

@login_required(login_url='/accounts/login/')
def StudentSearch(request):
    form_class= SearchForm
    form1=form_class(request.POST)

    if request.method=='POST':

        if form1.is_valid():
            form1.save(commit=True)
            return redirect('course:studentlist')


    else:
        form1= InitialForm()
    return render(request,'course/studentsearch.html',{'form1':form1})

@login_required(login_url='/accounts/login/')
def StudentList(request):
    x= Initial.objects.filter().order_by('-id')[0]
    z=  Initial.objects.filter().order_by('-id')[1]
    print(x,z)
    my_dict={'x':x,'z':z}
    print(my_dict["x"].Department)
    print(my_dict["x"].Semester)
    sem=my_dict["x"].Semester
    dep=my_dict["x"].Department
    y= Registration.objects.filter(Department=my_dict["x"].Department,Semester=my_dict["x"].Semester)
    s=  Registration.objects.filter(Department=my_dict["x"].Department,Semester=my_dict["x"].Semester).count()
    return render(request,'course/studentlist.html',{'y':y,'sem':sem,'dep':dep,'s':s})

@login_required(login_url='/accounts/login/')
def AddCourse(request):
    form_class= CoursesForm
    form=form_class(request.POST)
    if request.method=='POST':

        if form.is_valid():
            form.save(commit=True)

            return redirect('course:open_list')
    else:
        form= CoursesForm()
    return render(request,'course/addcourse.html',{'form':form})

@login_required(login_url='/accounts/login/')
def RegOpen(request):
    return render(request,'course/regopen.html')

@login_required(login_url='/accounts/login/')
def StudentDelete(request):
    form_class= Deleteform
    form1=form_class(request.POST)

    if request.method=='POST':

        if form1.is_valid():
            form1.save(commit=True)
            x= OnlySemester.objects.filter().order_by('-id')[0]
            my_dict={'x':x}
            Registration.objects.filter(Semester=my_dict["x"].Semester).delete()
            return redirect('course:regopen')


    else:
        form1= Deleteform()
    return render(request,'course/studentdelete.html',{'form1':form1})

@login_required(login_url='/accounts/login/')
def UpdateSemester(request):
    form_class= OpenForm
    form1=form_class(request.POST)

    if request.method=='POST':

        if form1.is_valid():
            Open.objects.filter(semester=form1.cleaned_data["semester"]).update(start_date=form1.cleaned_data["start_date"],finish_date=form1.cleaned_data["finish_date"])

            return redirect('course:regopen')


    else:
        form1= OpenForm()
    return render(request,'course/updatesemester.html',{'form1':form1})
    
@login_required(login_url='/accounts/login/')
def AddOptionalCourse(request):
    form_class= OptionalCourseForm
    form=form_class(request.POST)
    if request.method=='POST':

        if form.is_valid():
            form.save(commit=True)

            return redirect('course:regopen')
    else:
        form= OptionalCourseForm()
    return render(request,'course/addoptionalcourse.html',{'form':form})
