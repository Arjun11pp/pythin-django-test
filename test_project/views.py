from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def actors_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM ACTOR")
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

    data = [dict(zip(columns, row)) for row in rows]
    return render(request, 'actors_list.html', {'data': data})

def view(request):
    li=list()
    li.append('name')
    #print(li)
    dict1 = [{
        'id': 1,
        'first_name': 'amal'
    },
    {
        'id':2,
        'fname':'aman'
    },
    {
        'id':3,
        'fname':'amen'
            }]
    
    return render(request, 'actors_list.html', {'data': dict1}) 
def login(request):
    userdata = [{
        'username': 'admin',
        'password': 'admin'
    }]
    return render(request, 'login.html',{'data': userdata})
def name(request):
    stud_name=['amal','aman','amen']
    return render(request, 'students_list.html', {'data': stud_name})

def stud_details(request):
    stud_details = [{
        'name': 'amal',
        'age': 22,
        'class': 'btech'
    },
    {
        'name': 'aman',
        'age': 22,
        'class': 'mca'
    },
    {
        'name': 'amen',
        'age': 22,
        'class': 'bca'
    }                
    ]
    return render(request, 'stud_details.html', {'data': stud_details})