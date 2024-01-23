from django.shortcuts import render, redirect
from .models import Student
from .forms import StdForm, StdModelForm

def home(request):
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


