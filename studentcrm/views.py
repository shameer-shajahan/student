from django.shortcuts import render,redirect,get_object_or_404

from django.views.generic import View

from studentcrm.forms import StudentForm,StudentUpdateForm,SignupForm,SigninForm

from studentcrm.models import Student

from django.db.models import Q

from django.contrib.auth.models import User


class StudentView(View):

    template_name="student_form.html"

    form_class=StudentForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render (request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            print(data)

            Student.objects.create(**data)   

            return redirect ("student_list") 

        return render (request,self.template_name,{"form":form_instance})
    
class StudentList(View):

    template_name=("student_list.html")

    def get(self,request,*arg,**kwargs):

        search_text=request.GET.get("filter")

        print(search_text)

        qs=Student.objects.all()

        all_name=Student.objects.values_list("name",flat=True).distinct()
   
        all_age=Student.objects.values_list("age",flat=True).distinct()
   
        all_standard=Student.objects.values_list("standard",flat=True).distinct()

        all_gender=Student.objects.values_list("gender",flat=True).distinct()
   
        all_address=Student.objects.values_list("address",flat=True).distinct()
   
        all_mobile=Student.objects.values_list("mobile",flat=True).distinct()

        all_email=Student.objects.values_list("email",flat=True).distinct()

        all_records=[]

        all_records.extend(all_name)

        all_records.extend(all_age)
        
        all_records.extend(all_standard)
        
        all_records.extend(all_gender)
        
        all_records.extend(all_address)
        
        all_records.extend(all_mobile)
        
        all_records.extend(all_email)



        if search_text:
            qs=qs.filter(

                Q(name__contains=search_text)|Q(age__contains=search_text)|Q(standard__contains=search_text)|Q(gender__contains=search_text)|Q(address__contains=search_text)|Q(mobile__contains=search_text)|Q(email__contains=search_text)
                
                )

        return render(request,self.template_name,{"data":qs,"records":all_records})
    
class StudentDetailView(View):

    template_name="student_detail.html"

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Student.objects.get(id=id)

        return render(request,self.template_name,{"data":qs}) 
    
class StudentDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Student.objects.get(id=id).delete()

        return redirect("student_list")
    
class StudentUpdateView(View):

    template_name="student_update.html"

    form_class=StudentUpdateForm

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        student_object=get_object_or_404(Student,id=id)

        form_instance=self.form_class(instance=student_object)

        return render (request,self.template_name,{"forms":form_instance})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        student_object=get_object_or_404(Student,id=id)

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES,instance=student_object)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("student_list")
        
        return render(request,self.template_name,{"forms":form_instance})

class SignupView(View):

    template_name="register.html"

    form_class=SignupForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            User.objects.create_user(**data)

            return redirect("signin")
    
        return render(request,self.template_name,{"form":form_instance})



class SigninView(View):

    template_name="signin.html"

    form_class=SigninForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class

        return render(request,self.template_name,{"form":form_instance})



