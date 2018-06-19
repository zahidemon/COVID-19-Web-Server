from django import forms
from django.core import validators
from course.models import Remind,Registration,Initial,Courses,OnlySemester,Open,OptionalCourse

class RemindForm(forms.ModelForm):
    class Meta():
        model= Remind
        fields= ('Email','Date')
        widgets= {
            'Date':forms.TextInput(attrs={'class':'textinputclass','placeholder':'YYYY-MM-DD'})
        }



class CoursesForm(forms.ModelForm):
    class Meta():

        model= Courses
        fields = '__all__'
        widgets= {
            'Title':forms.TextInput(attrs={'class':'textinputclass'}),
        }
class OptionalCourseForm(forms.ModelForm):
    class Meta():

        model= OptionalCourse
        fields = '__all__'
        widgets= {
            'Title':forms.TextInput(attrs={'class':'textinputclass'}),
        }


class RegistrationForm(forms.ModelForm):

    class Meta():

        model= Registration
        fields= ('Semester','Department','Name','Roll','Credit','Backlogs')
        widgets={
            'Name':forms.TextInput(attrs={'class':'textinputclass'}),
            'Credit':forms.TextInput(attrs={'class':'textinputclass','placeholder':'Previously Earned Credit'}),
            'Backlogs':forms.TextInput(attrs={'class':'textinputclass','placeholder':'EX: CSE 1101, ME 1101'}),
            'Roll':forms.TextInput(attrs={'class':'textinputclass','placeholder':'Enter your Roll'}),

            }
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        s= cleaned_data['Roll']

        try:
            Registration.objects.get(Roll=s)
            raise forms.ValidationError('There is already a startup note for this year')
        except Registration.DoesNotExist:
            pass

        return cleaned_data



class InitialForm(forms.ModelForm):
    class Meta():
        model= Initial
        fields=('Semester','Department')

class SearchForm(forms.ModelForm):
    class Meta():
        model= Initial
        fields=('Semester','Department')

class Deleteform(forms.ModelForm):
    class Meta():
        model= OnlySemester
        fields=('Semester',)

class OpenForm(forms.ModelForm):
    class Meta():
        model= Open
        fields= ('semester','start_date','finish_date')
        widgets= {
            'start_date':forms.TextInput(attrs={'class':'textinputclass','placeholder':'YYYY-MM-DD'}),
            'finish_date':forms.TextInput(attrs={'class':'textinputclass','placeholder':'YYYY-MM-DD'})

        }
