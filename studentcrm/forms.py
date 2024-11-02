from django import forms

from studentcrm.models import Student

class StudentForm(forms.Form):

    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    age=forms.CharField()

    standard=forms.CharField()

    gender=forms.ChoiceField(choices=Student.gender_option)

    address=forms.CharField()

    mobile=forms.CharField()

    email=forms.EmailField()

    picture=forms.ImageField()

class StudentUpdateForm(forms.ModelForm):

    class Meta:

        model=Student

        fields="__all__"

        widgets={
            
            "name":forms.TextInput(attrs={"class":"form-control"}),

            "age":forms.TextInput(attrs={"class":"form-control"}),

            "standard":forms.TextInput(attrs={"class":"form-control"}),

            "gender":forms.Select(attrs={"class":"form-control"}),

            "address":forms.Textarea(attrs={"class":"form-control","rows":5}),
            
            "mobile":forms.NumberInput(attrs={"class":"form-control"}),
            
            "email":forms.EmailInput(attrs={"class":"form-control"}),
                        
            "picture":forms.FileInput(attrs={"class":"form-control"})
            
    
        }






