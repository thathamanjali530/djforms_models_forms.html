from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_student(request):
    SFEO=StudentForm()
    d={'SFEO':SFEO}

    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            sname=SFDO.cleaned_data['sname']
            sid=SFDO.cleaned_data['sid']
            semail=SFDO.cleaned_data['semail']
            SO=Student.objects.get_or_create(sname=sname,sid=sid,semail=semail)[0]
            SO.save()
            return HttpResponse('data inserted successfully')
    

    return render(request,'insert_student.html',d)