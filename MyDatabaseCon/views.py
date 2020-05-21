from django.shortcuts import render
from MyDatabaseCon.models import studentdata
from django.db import connection
from MyDatabaseCon.forms import student_form
# Create your views here.

def index(request):
	return render(request, "index.html")



def create(request):

	sd = studentdata()
	sd.rollno = request.POST["roll"]
	sd.name = request.POST["name"]
	sd.branch = request.POST["branch"]

	sd.save()

	return render(request, "create_records.html", context={'create_std': 'Record Saved successfully'})

def read(request):
	data = studentdata.objects.all()
	return render(request, "read_records.html", context={'read_std': data})

def update(request):
	data= studentdata.objects.filter(name='janardhan').update(branch='mca')
	return render(request, "update_records.html", context={'update_std': data})

def delete(request):
	data = studentdata.objects.filter(branch='cse').delete()
	return render(request, "delete_records.html", context={'delete_std': data})



def getform(request):

	if request.method == "POST":
		form = student_form(request.POST)
		if form.is_valid():
			sd = studentdata()
			sd.rollno = form.cleaned_data['Roll No']
			sd.name = form.cleaned_data["Name"]
			sd.branch = form.cleaned_data["Branch"]

			sd.save()
			return render(request, 'text.html', context={'status': 'data inserted'})

		else:
			form = student_form()
			return render(request, 'text.html', context={'form': form})
