# example/views.py
import sqlite3
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from example.models import Student, Teacher
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from . import *;
import subprocess
def view(request):
    return render(request,'templates/index.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        script_path = 'example/create.py'
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        dbase = sqlite3.connect('datab.sqlite3')
        cursor = dbase.cursor()
        cursor.execute("SELECT * FROM Student WHERE username = ?", (username,))
        user_data = cursor.fetchone()
        if(user_data):
                db_username = user_data[0]
                db_password = user_data[1]
                name = user_data[2]
                phone = user_data[3]
                if password == db_password:
                    # Successful login logic
                    return student_view(request)
                else:
                    #return JsonResponse({"status":"user_data"})
                    return render(request, 'templates/index.html')
        else:
            return render(request, 'templates/index.html')

    else:
        return render(request, 'templates/student_list.html')
def sign_view(request):
    if request.method == 'POST':
        username = request.POST.get('username1','')
        password = request.POST.get('password1','')
        # Connect to your custom users database
        script_path = 'example/create.py'  # Replace this with the actual path to create.py
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        dbase = sqlite3.connect('datab.sqlite3')
        cursor = dbase.cursor()
        cursor.execute("SELECT * FROM Student WHERE username = ?", (username,))
        user_data = cursor.fetchone()
        if(user_data):
                db_username = user_data[0]
                db_password = user_data[1]
                name = user_data[2]
                phone = user_data[3]
                if password == db_password:
                    # Successful login logic
                    return teacher_view(request)
                else:
                    return render(request,'templates/index.html')
                    #return login_view(request)
        else:
            return login_view(request)
            #return render(request, 'templates/index.html')

    else:
        return render(request, 'templates/index.html')
def student_view(request):
    username = request.POST['username']
    dbase = sqlite3.connect('datab.sqlite3')
    cursor = dbase.cursor()
    cursor.execute("SELECT * FROM Student WHERE username = ?", (username,))
    students = cursor.fetchone()
    s=students[2]
    return render(request,'templates/student_list.html',{'data': s})
def teacher_view(request):
    username = request.POST['username1']
    dbase = sqlite3.connect('datab.sqlite3')
    cursor = dbase.cursor()
    cursor.execute("SELECT * FROM Student WHERE username = ?", (username,))
    teachers= cursor.fetchone()
    return render(request,'templates/teacher_list.html',{'bata': teachers})
