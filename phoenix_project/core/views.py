from django.shortcuts import render,redirect
from .models import User
from .forms import detailsform

from decimal import Decimal
# Create your views here.

default_dict = {
    'acc_page' : ['index']
}
def index(request):
    try:
        user = User.objects.get(email = request.session['email'])
        if user:
            return render(request, 'Details.html',default_dict)
        else:
            return redirect(index)
    except Exception as e:
        print(f"\n\n\n{e}\n\n\n")
        default_dict['current_page'] = 'index'
        return render(request, 'Details.html',default_dict)


def register_page(request):
    default_dict['current_page'] = 'register_page'

    if request.method == "POST":
        try:
            user = User.objects.get(email = request.POST['email'])
            msg = "User already exists"
            default_dict['msg_s'] = msg

            return render(request, 'login_page.html',default_dict)
        except:
            if request.POST["password"] is None:

                msg = "All fields are mendatory"
                default_dict['msg_d'] = msg

                return render(request, 'register_page.html',default_dict)

            elif request.POST['password'] == request.POST['confirm_password']:

                user = User.objects.create(
                    email = request.POST['email'],
                    password = request.POST['password']
                )

                user.save()
                msg = "Sign Up was successful."
                default_dict['msg_s'] = msg

                return render(request, 'login_page.html',default_dict)
            else:
                msg = "Password and confirm password does not match"
                default_dict['msg_d'] = msg
                return render(request, 'register_page.html',default_dict)
            
    else:
        return render(request, 'register_page.html',default_dict)

def login_page(request):
    default_dict['current_page'] = 'login_page'

    if request.method == "POST":
        try:
            user = User.objects.get(email = request.POST['email'],password = request.POST['password'])
            request.session['email'] = user.email
            return redirect(index)
        
        except:
            msg = "Invalid Email or Password"
            default_dict['msg_d'] = msg
            return render(request, "login_page.html",default_dict)
    else:
        return render(request, 'login_page.html',default_dict)

def create(request):
    # print(requests.session['email'])
    user = User.objects.get(email = request.session['email'])
    print(user)
    if request.method=="POST":
        user.full_name=request.POST['full_name']
        user.city= request.POST['city']
        user.state = request.POST['state']
        user.county = request.POST['county']
        user.vat_rate = request.POST['vat_rate']
        user.save()
        return redirect(retrieve)
    else:
        return render(request, 'Details.html')
    
def retrieve(request):
    details=User.objects.all()
    return render(request,'retrieve.html',{'details':details})


def edit(request,id):
    object=User.objects.get(id=id)  
    return render(request,'edit.html',{'object':object})
    # else:
    #     return render(request,'edit.html')
        
    
def update(request,id):
    object=User.objects.get(id=id)
    form=detailsform(request.POST,instance=object)
    if form.is_valid:
        form.save()
        object=User.objects.all()
        return redirect('retrieve')



def delete(request, pk):
    employee = User.objects.get(id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('retrieve')

    context = {
        'employee': employee,
    }
    return render(request, 'delete.html', context)

