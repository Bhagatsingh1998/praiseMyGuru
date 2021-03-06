from django.shortcuts import render, redirect
from .models import AddTeacher, AddCollege, AddSchool
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from accounts.models import Signups

# Create your views here.

@login_required(login_url='signin')
def addTeacher(request) :
  if request.method == 'POST' :
    # current_userID = request.user.pk
    current_userID = Signups.objects.get(userName = request.user.username)
    # current_userID = Signups.objects.get(id = current_user +1)
    # user = User.objects.get(id=user_id)
    # staffprofile.user = user
    # if request.user.is_authenticated :
      # current_userID = request.user.id

    fname = request.POST['firstname']
    lname = request.POST['lastname']
    institute_type = request.POST['Institutetype']
    institute_name = request.POST['institudename']
    subjects = request.POST.getlist('subjects')
    age = request.POST['age']
    expirance = request.POST['expirance']

    uplaodedFile = request.FILES['imgupload']
    fs = FileSystemStorage()
    imgname = fs.save(uplaodedFile.name, uplaodedFile)
    url = fs.url(imgname)
    # , userID = current_userID
    teachermoto = request.POST['teachermoto']
    dateTime = timezone.now()
    addteacher = AddTeacher(userID = current_userID, firstName = fname, lastName = lname, instituteType = institute_type, institute = institute_name, subjects = subjects, age = age, image = url, expirence = expirance,  moto = teachermoto, dateTime = dateTime)
    addteacher.save()
    return redirect('home')

  else :
    return render(request, 'add/addTeacher.html')

@login_required(login_url='signin')
def addSchool(request) :
  if request.method == 'POST' :
    current_userID = Signups.objects.get(userName = request.user.username)
    name = request.POST['name']
    location = request.POST['location']
    types = request.POST.getlist('colg')
    describe = request.POST['rate']
    website = request.POST['website']
    phone = request.POST['phoneno']
    founded = request.POST['year']
    dateTime = timezone.now();
    
    # uplaodedFile1 = request.FILES['pic1']
    # fs1 = FileSystemStorage()
    # imgname1 = fs1.save(uplaodedFile1.name, uplaodedFile1)
    # url1 = fs1.url(imgname1) 
    # image1 = url1, 

    schoolinfo = AddSchool(userID = current_userID, name = name, location = location, types = types, describe = describe, website = website, phone = phone, founded = founded, dateTime = dateTime)
    schoolinfo.save()
    return redirect('home')
  else:
    return render(request, 'add/addSchool.html')

@login_required(login_url='signin')
def addCollege(request) :
  if request.method == 'POST' :
    current_userID = Signups.objects.get(userName = request.user.username)
    name = request.POST['name']
    location = request.POST['location']
    types = request.POST.getlist('colg')
    describe = request.POST['rate']
    website = request.POST['website']
    phone = request.POST['phoneno']
    founded = request.POST['year']

    # college = request.FILES
    # uplaodedFile2 = college['pic2']
    # uplaodedFile2 = request.FILES['pic2']
    # fs2= FileSystemStorage()
    # imgname2 = fs2.save(uplaodedFile2.name,  uplaodedFile2)
    # url2 = fs2.url(imgname2) 
    # image2 = url2,

    dateTime = timezone.now();
    collegeinfo = AddCollege(userID = current_userID, name = name, location = location, types = types, describe = describe, website = website, phone = phone, founded = founded, dateTime = dateTime)
    collegeinfo.save()
    return redirect('home')
  else:
    return render(request, 'add/addCollege.html')