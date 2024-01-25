from django.shortcuts import render, redirect
from .models import Student
from .forms import StdForm, StdModelForm
from rest_framework.response import Response
from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view
from .serializers import BaseStudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.core.mail import EmailMessage
from rest_framework.views import APIView

def home(request):
    # email = EmailMessage('Django Email Test Title', 'Test Content', to=['ppy040@naver.com'])
    # email.send()
    return render(request, 'index.html')

def create_html_form(request):
    if request.method == 'POST':
        std = Student()
        std.studentID = request.POST['studentID']
        std.name = request.POST['name']
        std.major = request.POST['major']
        std.save()
    
    return redirect('home')

def create_django_form(request):
    # POST라면 입력한 내용을 form을 이용하여 데이터베이스에 저장
    if request.method == 'POST':
        form = StdForm(request.POST)
    
        # 유효성 검사
        if form.is_valid():
            std = Student()
            std.studnetID = form.cleaned_data['studentID']
            std.name = form.cleaned_data['name']
            std.major = form.cleaned_data['major']
            std.save()
            return redirect('home')
    # GET이면 입력값을 받을 수 있는 html을 가져다 줘야 함
    else:
        form = StdForm()
    
    return render(request, 'django_form_create.html', {'form':form})

def create_model_form(request):
    # POST라면 입력한 내용을 form을 이용하여 데이터베이스에 저장
    if request.method == 'POST' or request.method == 'FILES':
        form = StdModelForm(request.POST, request.FILES)
    
        # 유효성 검사
        if form.is_valid():
            form.save()
            return redirect('home')
    
    # GET이면 입력값을 받을 수 있는 HTML을 가져다 줘야 함
    else:
        form = StdModelForm()
    
    return render(request, 'model_form_create.html', {'form': form})

@api_view(['GET'])
def student_detail(request, id):
    student = Student.objects.get(id=id)
    serializer = BaseStudentSerializer(student)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        stdList = Student.objects.all()
        serializer = BaseStudentSerializer(stdList, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BaseStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudnetDetial(APIView):
    # Student 객체 가져오기
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist: # 오류가 발생하면(객체가 존재하지 않으면) DoNotExist 에러를 반환
            raise Http404
    
    # Student 객체의 Detail 반환 (GET)
    def get(self, request, pk, format=None): # format=None은 url 패턴과 관련!
        student = self.get_object(pk)
        serializer = BaseStudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Student 객체 수정 (PUT)
    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = BaseStudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    # Student 객체 삭제 (DELETE)
    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Blog의 목록을 보여주는 역할
class StudentList(APIView):
    # student list (GET)
    def get(self, request):
        students = Student.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = BaseStudentSerializer(students, many=True)
        return Response(serializer.data)

    # 새로운 student를 생성 (POST)
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = BaseStudentSerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)