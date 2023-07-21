from math import sqrt
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import UserForm
from .models import Coeficientes


# Create your views here.
def baskara_view(request):
    #Faz a primeira renderização ao acessar a página
    if request.method == "GET":
        
        form = UserForm()
        context = {
            'form':form
        }
        return render(request,'calculo/index.html', context=context)
    else:
        form = UserForm(request.POST)   
        if form.is_valid():            
            a = request.POST.get('a')
            b = request.POST.get('b')
            c = request.POST.get('c')

            delta = (float(b)*float(b)) - 4*float(a)*float(c)

            x1 = (-float(b)+ sqrt(delta)) / (2.0*float(a))
            x2 = (-float(b)- sqrt(delta)) / (2.0*float(a))

            if delta > 0:
                resultado = f"Duas raízes {x1} e {x2}"
                try:
                    ans = eval(resultado)
                    mydictionary ={
                        "resultado": resultado,
                        "ans": ans,
                        "error":error
                    }
                    return render(request,"calculo/index.html",context=mydictionary)
                except:
                    pass
            elif delta == 0:
                resultado = f"Uma raíz real {x1}"
                try:
                    ans = eval(resultado)
                    mydictionary ={
                        "resultado": resultado,
                        "ans": ans,
                        "error":error
                    }
                    return render(request,"calculo/index.html",context=mydictionary)
                except:
                    pass

            else:
                resultado = f"sem raízes reais"
                try:
                    ans = eval(resultado)
                    mydictionary ={
                        "resultado": resultado,
                        "ans": ans,
                        "error":error
                    }
                    return render(request,"calculo/index.html",context=mydictionary)
                except:
                    pass


            context={
                'form' : form,
                'x1': x1,
                'x2': x2,
                'resultado':resultado,
            }

            return render(request,'calculo/index.html', context=context)
        

    
