from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# --- REGISTER VIEW ---
def regi_view(request):
    if request.method == 'POST': 
        Student.objects.create(
            studentname=request.POST.get('studentname'),
            rollnumber=request.POST.get('rollnumber'),
            password=request.POST.get('password')
        )
        return redirect('login')
    return render(request, 'index.html')
@api_view(['POST'])
def regi_serializer(request):
    if request.method=='POST':
        student= StudentSerializer(data=request.data)
        student.is_valid()
        student.save()
        return Response(student.data,status=200)
    return Response(student.errors,status=400)
    
    
    

# --- LOGIN VIEW ---
def login_view(request):
    if request.method == "POST":
        user_roll = request.POST.get('rollnumber')
        passw = request.POST.get('password')

        if Student.objects.filter(rollnumber=user_roll, password=passw).exists():
            return redirect('home') 
        else:
            return HttpResponse("User does not exist or wrong password!")
    return render(request, 'login.html')

@api_view(['POST'])
def login_api_view(request):
    if request.method=='POST':
        user_roll=request.data.get('rollnumber')
        passw=request.data.get('password')
        student=Student.objects.filter(rollnumber=user_roll,password=passw).first()
        if student:
            seri=StudentSerializer(student)
            return Response(seri.data,status=200)
        else:
            return Response(seri.error,status=401)
    return Response(request)
          
    
# --- HOME VIEW (Read) ---
#__________selecting all students__________
def home_view(request):
    all_students = Student.objects.all()
    search_id = request.GET.get('id') 
    if search_id:
        all_students = all_students.filter(rollnumber=search_id) 
    context = {'students': all_students}
    return render(request, 'home.html', context)
@api_view(['GET'])
def home_api_view(request):
    if request.method=='GET':
        student=Student.objects.all()
        seri=StudentSerializer(student,many=True)
        return Response(seri.data,status=200)
    return Response(seri.error,status=400)
    
#__________update one student__________
def update_view(request):
    if request.method == 'POST':
        target_roll = request.POST.get('id') 
        new_name = request.POST.get('update') 
        new_roll = request.POST.get('new_roll_input') 
        try:
            student = Student.objects.get(rollnumber=target_roll) 
            if new_name:
                student.studentname = new_name
            if new_roll:
                student.rollnumber = new_roll
            student.save()
            return redirect('home') 
        except Student.DoesNotExist:
            return HttpResponse("The roll number you entered does not exist!")
    return redirect('home')
@api_view(['PUT'])
def update_api_view(request, pk): # We pass 'pk' from the URL
    try:
        # 1. The Search (Inside the try block)
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)

    # 2. The Translator
    # 'partial=True' means we can update JUST the name without the password
    seri = StudentSerializer(instance=student, data=request.data, partial=True)

    # 3. The Guard
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=200)
    else:
        # Tell the AI/App exactly what was wrong with their data
        return Response(seri.errors, status=400)
        
            
            
#____________delete one student__________
def delete_view(request):
    try:
        if request.method=='POST':
            roll=request.POST.get('id')
            delete_row=Student.objects.get(rollnumber=roll)
            delete_row.delete()
            return render(request,'home.html')
    except Student.DoesNotExist:
        return HttpResponse('not exist')
    return redirect('home')

@api_view(['DELETE'])
def delete_api_view(request, pk):
    try:
        student_to_delete = Student.objects.get(pk=pk)
        student_to_delete.delete()
        return Response({"message": "Successfully deleted"}, status=204)  
    except Student.DoesNotExist:

        return Response({"error": "ID not found"}, status=404)
    
    
        
    
        
            