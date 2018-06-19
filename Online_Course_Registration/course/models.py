from django.db import models
from django import forms
from django.utils import timezone
from uuid import uuid4

def generateUUID():
    return str(uuid4())

# Create your models here.
class Courses(models.Model):
    cse='CSE'
    eee='EEE'
    me='ME'
    civil='CE'
    mecha='MTE'
    glass= 'GCE'
    ece='ECE'
    ete='ETE'
    arch= 'ARCH'
    urp='URP'
    becm= 'BECM'
    mse='MSE'
    ipe='IPE'
    cfpe= 'CFPE'

    odd1='1st Year Odd Semester'
    even1='1st Year Even Semester'
    odd2='2nd Year Odd Semester'
    even2='2nd Year Even Semester'
    odd3='3rd Year Odd Semester'
    even3='3rd Year Even Semester'
    odd4='4th Year Odd Semester'
    even4='4th Year Even Semester'

    c=(
    (cse,'CSE'),
    (eee,'EEE'),
    (me,'ME'),
    (civil,'CE'),
    (mecha,'MTE'),
    (glass,'GCE'),
    (ece,'ECE'),
    (ete,'ETE'),
    (arch,'ARCH'),
    (urp,'URP'),
    (becm,'BECM'),
    (mse,'MSE'),
    (ipe,'IPE'),
    (cfpe,'CFPE'),
    )

    d=(
        (odd1,'1st Year Odd Semester'),
        (even1,'1st Year Even Semester'),
        (odd2,'2nd Year Odd Semester'),
        (even2,'2nd Year Even Semester'),
        (odd3,'3rd Year Odd Semester'),
        (even3,'3rd Year Even Semester'),
        (odd4,'4th Year Odd Semester'),
        (even4,'4th Year Even Semester'),
    )
    x=(
        ("Compulsory","Compulsory"),
        ("Optional","Optional"),
    )

    Course_id = models.CharField(max_length=256)
    Title = models.CharField(max_length=256)
    Credit = models.FloatField()
    Semester = models.CharField(max_length=256,choices=d,default=odd1)
    Department = models.CharField(max_length=256, choices=c,default=cse)

    def __str__(self):
        return '%s %s %s %s' % (self.Title, self.Department, self.Semester, self.Course_id)

class Open(models.Model):
    odd1='1st Year Odd Semester'
    even1='1st Year Even Semester'
    odd2='2nd Year Odd Semester'
    even2='2nd Year Even Semester'
    odd3='3rd Year Odd Semester'
    even3='3rd Year Even Semester'
    odd4='4th Year Odd Semester'
    even4='4th Year Even Semester'
    d=(
        (odd1,'1st Year Odd Semester'),
        (even1,'1st Year Even Semester'),
        (odd2,'2nd Year Odd Semester'),
        (even2,'2nd Year Even Semester'),
        (odd3,'3rd Year Odd Semester'),
        (even3,'3rd Year Even Semester'),
        (odd4,'4th Year Odd Semester'),
        (even4,'4th Year Even Semester'),
    )
    semester = models.CharField(max_length=256,choices=d,default=odd1)
    start_date= models.DateField()
    finish_date= models.DateField()

class Remind(models.Model):
    Email= models.EmailField()
    Date= models.DateField()



class Registration(models.Model):
    cse='CSE'
    eee='EEE'
    me='ME'
    civil='CE'
    mecha='MTE'
    glass= 'GCE'
    ece='ECE'
    ete='ETE'
    arch= 'ARCH'
    urp='URP'
    becm= 'BECM'
    mse='MSE'
    ipe='IPE'
    cfpe= 'CFPE'

    odd1='1st Year Odd Semester'
    even1='1st Year Even Semester'
    odd2='2nd Year Odd Semester'
    even2='2nd Year Even Semester'
    odd3='3rd Year Odd Semester'
    even3='3rd Year Even Semester'
    odd4='4th Year Odd Semester'
    even4='4th Year Even Semester'

    c=(
    (cse,'CSE'),
    (eee,'EEE'),
    (me,'ME'),
    (civil,'CE'),
    (mecha,'MTE'),
    (glass,'GCE'),
    (ece,'ECE'),
    (ete,'ETE'),
    (arch,'ARCH'),
    (urp,'URP'),
    (becm,'BECM'),
    (mse,'MSE'),
    (ipe,'IPE'),
    (cfpe,'CFPE'),
    )

    d=(
        (odd1,'1st Year Odd Semester'),
        (even1,'1st Year Even Semester'),
        (odd2,'2nd Year Odd Semester'),
        (even2,'2nd Year Even Semester'),
        (odd3,'3rd Year Odd Semester'),
        (even3,'3rd Year Even Semester'),
        (odd4,'4th Year Odd Semester'),
        (even4,'4th Year Even Semester'),
    )



    Semester = models.CharField(max_length=256,choices=d,default=odd1)
    Department = models.CharField(max_length=256, choices=c,default=cse)
    Name= models.CharField(max_length=256)
    Roll= models.CharField(max_length=7)
    Credit= models.FloatField()
    Backlogs= models.TextField(max_length=256,blank=True)
    Courses= models.CharField(max_length=512,default="Some String")



    def __str__(self):
        return '%s %s %s %s %s' % (self.Semester, self.Department, self.Name,self.Roll,self.Courses)

class Initial(models.Model):
    cse='CSE'
    eee='EEE'
    me='ME'
    civil='CE'
    mecha='MTE'
    glass= 'GCE'
    ece='ECE'
    ete='ETE'
    arch= 'ARCH'
    urp='URP'
    becm= 'BECM'
    mse='MSE'
    ipe='IPE'
    cfpe= 'CFPE'

    odd1='1st Year Odd Semester'
    even1='1st Year Even Semester'
    odd2='2nd Year Odd Semester'
    even2='2nd Year Even Semester'
    odd3='3rd Year Odd Semester'
    even3='3rd Year Even Semester'
    odd4='4th Year Odd Semester'
    even4='4th Year Even Semester'

    c=(
    (cse,'CSE'),
    (eee,'EEE'),
    (me,'ME'),
    (civil,'CE'),
    (mecha,'MTE'),
    (glass,'GCE'),
    (ece,'ECE'),
    (ete,'ETE'),
    (arch,'ARCH'),
    (urp,'URP'),
    (becm,'BECM'),
    (mse,'MSE'),
    (ipe,'IPE'),
    (cfpe,'CFPE'),
    )

    d=(
        (odd1,'1st Year Odd Semester'),
        (even1,'1st Year Even Semester'),
        (odd2,'2nd Year Odd Semester'),
        (even2,'2nd Year Even Semester'),
        (odd3,'3rd Year Odd Semester'),
        (even3,'3rd Year Even Semester'),
        (odd4,'4th Year Odd Semester'),
        (even4,'4th Year Even Semester'),
    )

    Semester = models.CharField(max_length=256,choices=d,default=odd1)
    Department = models.CharField(max_length=256, choices=c,default=cse)


class OnlySemester(models.Model):
    odd1='1st Year Odd Semester'
    even1='1st Year Even Semester'
    odd2='2nd Year Odd Semester'
    even2='2nd Year Even Semester'
    odd3='3rd Year Odd Semester'
    even3='3rd Year Even Semester'
    odd4='4th Year Odd Semester'
    even4='4th Year Even Semester'

    d=(
        (odd1,'1st Year Odd Semester'),
        (even1,'1st Year Even Semester'),
        (odd2,'2nd Year Odd Semester'),
        (even2,'2nd Year Even Semester'),
        (odd3,'3rd Year Odd Semester'),
        (even3,'3rd Year Even Semester'),
        (odd4,'4th Year Odd Semester'),
        (even4,'4th Year Even Semester'),
    )

    Semester = models.CharField(max_length=256,choices=d,default=odd1)

class OptionalCourse(models.Model):
    cse='CSE'
    eee='EEE'
    me='ME'
    civil='CE'
    mecha='MTE'
    glass= 'GCE'
    ece='ECE'
    ete='ETE'
    arch= 'ARCH'
    urp='URP'
    becm= 'BECM'
    mse='MSE'
    ipe='IPE'
    cfpe= 'CFPE'

    odd1='1st Year Odd Semester'
    even1='1st Year Even Semester'
    odd2='2nd Year Odd Semester'
    even2='2nd Year Even Semester'
    odd3='3rd Year Odd Semester'
    even3='3rd Year Even Semester'
    odd4='4th Year Odd Semester'
    even4='4th Year Even Semester'

    c=(
    (cse,'CSE'),
    (eee,'EEE'),
    (me,'ME'),
    (civil,'CE'),
    (mecha,'MTE'),
    (glass,'GCE'),
    (ece,'ECE'),
    (ete,'ETE'),
    (arch,'ARCH'),
    (urp,'URP'),
    (becm,'BECM'),
    (mse,'MSE'),
    (ipe,'IPE'),
    (cfpe,'CFPE'),
    )

    d=(
        (odd1,'1st Year Odd Semester'),
        (even1,'1st Year Even Semester'),
        (odd2,'2nd Year Odd Semester'),
        (even2,'2nd Year Even Semester'),
        (odd3,'3rd Year Odd Semester'),
        (even3,'3rd Year Even Semester'),
        (odd4,'4th Year Odd Semester'),
        (even4,'4th Year Even Semester'),
    )
    x=(
        ("Optional I","Optional I"),
        ("Optional II","Optional II"),
    )

    Type= models.CharField(max_length=256,choices=x,default="Optional I")
    Course_id = models.CharField(max_length=256,unique=True)
    Title = models.CharField(max_length=256)
    Credit = models.FloatField()
    Semester = models.CharField(max_length=256,choices=d,default=odd1)
    Department = models.CharField(max_length=256, choices=c,default=cse)

    def __str__(self):
        return '%s %s %s %s' % (self.Title, self.Department, self.Semester, self.Type)
