from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserFormsModel


from .forms import *

# Create your views here.



def update(request, pk):
    user_id = User.objects.get(id=pk)
    form = UserFormsModel(instance=user_id)
    
    if request.method == "POST":
        form = UserFormsModel(request.POST, instance=user_id)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'utilisateur/update.html', context)

# def edit(request):
#     if request.method == 'POST':
        
#         print(f"request post : {request.POST}")
#         form = UserFormsModel(request.POST)
#         if form.is_valid():
#             # print(f"form : {form} ")
#             form.save()
#             return redirect('utilisateur:list')
    
#     form=UserFormsModel()
    
#     context = {'form':form}

#     return render(request, 'utilisateur/edit.html',context)



def edit(request):
    if request.method =='POST':
        pseudo= request.POST['username']
        password=request.POST['password']
        print(request.POST)
        if not pseudo or not password:
            return redirect('utilisateur:list')
        user=User(username=pseudo)
        user.save()
        user.password=password
        user.set_password(user.password)
        user.save()
        
    
    return render(request, 'utilisateur/edit.html')



def list(request):
    utilisateur=User.objects.all()
    
    return render(request, 'utilisateur/list.html', {'utilisateur': utilisateur})



def delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
    return render(request, 'utilisateur/delete.html', {'utilisateur': user})



