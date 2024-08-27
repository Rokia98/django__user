from django.shortcuts import redirect, render ,get_object_or_404
from .forms import TeacherForm
from .models import Teacher

# Create your views here.
def update(request, pk):

    teacher_id = Teacher.objects.get(id=pk)
    form = TeacherForm(instance=teacher_id)
    
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher_id)
        if form.is_valid():
            form.save()
    context = {'form':form}

    return render(request, 'utilisateur/update.html', context)

def edit(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('professeur:list')

    form = TeacherForm()
    context = {'form':form}

    return render(request, 'professeur/edit.html', context)



def list(request):
    teachers=Teacher.objects.all()
    
    return render(request, 'professeur/list.html', {'teacher': teachers})



def delete(request, pk):
    teacher= get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
    return render(request, 'professeur/delete.html', {'teacher': teacher})


