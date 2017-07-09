from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login

from mains.models import *


@csrf_exempt
def Login(request):
    if request.POST:
        try:
            email = request.POST['email']
            password = request.POST['password']
            member = authenticate(email=email, password=password, )
            if member is not None:
                login(request, member)
                return JsonResponse({'result': 'success'})
            else:
                return JsonResponse({'result': 'error'})
        except:
            return JsonResponse({'result': 'error'})
    else:
        return render(request, 'pages/teacher_login.html')


@csrf_exempt
def Signup(request):
    if request.POST:
        try:
            Teacher.objects.get(email=request.POST['email'])
            return JsonResponse({'result': 'error', 'message': '아이디가 중복됩니다. 메인 페이지에서 로그인 해주세요.'}, )
        except:
            parent = Teacher.createTeacher(request.POST['email'], request.POST['corporation'],
                                           request.POST['birthday'], request.POST['password1'])
            return JsonResponse({'result': 'success'})
    else:
        return render(request, 'pages/teacher_singup.html')


@csrf_exempt
def CheckEmail(request):
    try:
        Teacher.objects.get(email=request.POST['email'])
        return JsonResponse({'result': 'error'})
    except:
        return JsonResponse({'result': 'success'})


@csrf_exempt
def CreateClass(request):
    try:
        teacher = Teacher.objects.get(id=request.user.id)
        classRoom = ClassRoom.objects.create(teacher=teacher, className=request.POST['className'],
                                             classInfo=request.POST['classInfo'], studentCount=0)
        classRoom.save()
        return JsonResponse({'result': 'success', 'classRoomId': classRoom.id})
    except:
        return JsonResponse({'result': 'error'})


def TeacherClass(request):
    teacher = Teacher.objects.get(id=request.user.id)
    classRooms = ClassRoom.objects.filter(teacher=teacher).order_by('-created')
    return render(request, 'pages/teacher_class.html', {'classRooms': list(classRooms)})


def CreatedClassRoom(request):
    classRoom = ClassRoom.objects.get(id=request.GET.get('classRoomId'))
    return render(request, 'pages/teacher_detail_class.html', {'classRoom': classRoom})


def DetailClassRoom(request):
    classRoom = ClassRoom.objects.get(id=request.GET.get('classRoomId'))
    students = Tbuser.objects.filter(clclassroom=classRoom.id).order_by('clname')
    return render(request, 'pages/teacher_detail_class_student_info.html', {'students': list(students), 'classRoomId': classRoom.id})


@csrf_exempt
def CreateStudent(request):
    try:
        print(request.POST)
        student = Tbuser.objects.create(claccount=request.POST['email'], clpassword="1234",
                                        clclassroom=request.POST['classRoomId'],
                                        clname=request.POST['name'], clinfo=request.POST['info'])
        student.save()
        return JsonResponse({'result': 'success'})
    except:
        return JsonResponse({'result': 'error'})