from django.shortcuts import get_object_or_404, redirect, render
from .forms import EleveForm
from .models import Student

# l'ensembles de fonction 
# Create your views here.

def edit(request):
    if request.method == 'POST':
        form = EleveForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Eleve:list')
    
    form = EleveForm()

    return render(request, 'Eleve/edit.html', {'form': form})


def update(request, pk):
    student_id = Student.objects.get(id=pk)
    form = EleveForm(instance=student_id)
    
    if request.method == "POST":
        form = EleveForm(request.POST, instance=student_id)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'Eleve/update.html', context)

def list(request):
    students=Student.objects.all()
    
    return render(request, 'Eleve/list.html', {'student': students})

def delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
    return render(request, 'Eleve/delete.html', {'student': student})










