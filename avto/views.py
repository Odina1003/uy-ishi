from django.shortcuts import render, redirect, get_object_or_404
from .models import Avtomobile
from .forms import Avto


# Create your views here.
def avtos(request):
    avtomobiles = Avtomobile.objects.all()
    return render(request=request, template_name='index.html', context={'avtomobiles':avtomobiles})

def avto_create(request):  
    if request.method == "POST":  
        form = Avto(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('avto-list')  
            except:  
                pass  
    else:  
        form = Avto()  
    return render(request=request, template_name='avto-create.html', context={'form':form}) 

def avto_delete(request, pk):
    post = get_object_or_404(Avtomobile, id=pk)
    post.delete()
    return redirect('/avtomobiles')