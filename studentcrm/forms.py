from django import forms

from studentcrm.models import Student

from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
     
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

class SignupForm(forms.ModelForm):

    class Meta:

        model=User

        fields=["username","email","password"]

        widgets={

        "username":forms.TextInput(attrs={"class" : "form-control"}),

        "email":forms.EmailInput(attrs={"class" : "form-control"}),

        "password":forms.PasswordInput(attrs={"class" : "form-control"})

        }


class SigninForm(forms.ModelForm):

    class Meta:

        model=User

        fields=["username","password"]

        widgets={

        "username":forms.TextInput(attrs={"class" : "form-control"}),

        "password":forms.PasswordInput(attrs={"class" : "form-control"})

        }








