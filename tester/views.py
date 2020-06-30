from django.shortcuts import render, redirect
from .models import Details,profile1,blog
from .forms import Detailsform,Profileform,Blogform
from django.contrib import messages

from django.contrib.auth.decorators import login_required


def base(request):
    return render(request,'basepage.html')

def happiness(request):
    return render(request,'happiness.html')

def motivation(request):
    return render(request,'motivation.html')

def relaxing(request):
    return render(request,'relaxing.html')

def music(request):
    return render(request,'music.html')

def about(request):
    return render(request,'about.html')

def sudohome(request):
    return render(request,'sudohome.html')

def viewprofile(request):
    pic=profile1.objects.all()
    return render(request,'viewprofile.html',{'p1':pic})

@login_required(login_url='users:login')
def edit(request,id):
    details=blog.objects.get(id=id)
    if request.method == 'POST':
        form=Blogform(request.POST,request.FILES,instance = details)
        if form.is_valid():  
            print('praneeth',form.errors)
            form.save()  
            return redirect("tester:details") 
    context={'details':details}
    
    return render(request,'edit.html',context)

@login_required(login_url='users:login')
def story(request,id):
    details=blog.objects.get(id=id)
    context={'details':details}
    return render(request,'story.html',context)

def home(request):
    pic=profile1.objects.all()[:2]
    return render(request,'homepage.html',{'p1':pic})

def uprofile(request):
    pic=profile1.objects.all()
    return render(request,'Profilepage.html',{'p1':pic})

def dele(request):  
    employee = profile1.objects.all() 
    employee.delete()  
    return render(request,'details.html')
@login_required(login_url='users:login')
def delete(request, id):  
    employee = blog.objects.get(id=id)  
    employee.delete()  
    return redirect("tester:details")

@login_required(login_url='users:login')
def details(request):
    details=blog.objects.filter(owner=request.user)
    context={'details':details}
    return render(request,'details.html',context)

@login_required(login_url='users:login')
def adddetails(request):
    if request.method != 'POST':
        
        print(request.method)
        form=Blogform()
    else:
        form=Blogform(request.POST,request.FILES)
        print(request.method)
        if form.is_valid():
            newform=form.save(commit=False)
            newform.owner=request.user
            newform.save()

            return redirect('tester:details')
    context={'form':form}
    print('prani',form.errors)
    return render(request,'adddetails.html',context)

@login_required(login_url='users:login')
def profile(request):
    if request.method != 'POST':
        
        print(request.method)
        form=Profileform()
    else:
        form=Profileform(request.POST,request.FILES)
        print(request.method)
        if form.is_valid():
            newform=form.save(commit=False)
            newform.owner=request.user
            newform.save()
            return redirect('users:login')
    context={'form':form}
    print('prani',form.errors)
    return render(request,'profile.html',context)

def homesudo(request):
    return render(request,'homesudo.html')

def success1(request):
    return render(request,'success.html')

def exam(request):
    return render(request,'exam.html')

def change(request):
    return render(request,'password_reset.html')

def sudo1(request):
    b=[]
    if request.method=="POST":
        for i in range(1,37):
            c=str(i)
            if i==3:
                b.append(int(3))
            elif i==6:
                b.append(int(1))
            elif i==7:
                b.append(int(6))
            elif i==15:
                b.append(int(2))
            elif i==23:
                b.append(int(4))
            elif i==28:
                b.append(int(6))
            elif i==32:
                b.append(int(6))
            else:
                b.append(int(request.POST[c]))
        if b[0]!=b[1] and b[0]!=b[2] and b[0]!=b[3] and b[0]!=b[4] and b[0]!=b[5]:
            if b[6]!=b[7] and b[6]!=b[8] and b[6]!=b[9] and b[6]!=b[10] and b[6]!=b[11]:
                if b[12]!=b[13] and b[12]!=b[14] and b[12]!=b[15] and b[12]!=b[16] and b[12]!=b[17]:
                    if b[18]!=b[19] and b[18]!=b[20] and b[18]!=b[21] and b[18]!=b[22] and b[18]!=b[23]:
                        if b[24]!=b[25] and b[24]!=b[26] and b[24]!=b[27] and b[24]!=b[28] and b[24]!=b[29]:
                            if b[30]!=b[31] and b[30]!=b[32] and b[30]!=b[33] and b[30]!=b[34] and b[30]!=b[35]:
                                if b[0]<7 and b[1]<7 and b[2]<7 and b[3]<7 and b[4]<7 and b[5]<7 and b[6]<7 and b[7]<7 and b[8]<7 and b[9]<7 and b[10]<7 and b[11]<7 and b[12]<7 and b[13]<7 and b[14]<7 and b[15]<7 and b[16]<7 and b[17]<7 and b[18]<7 and b[19]<7 and b[20]<7 and b[21]<7 and b[22]<7 and b[23]<7 and b[24]<7 and b[25]<7 and b[26]<7 and b[27]<7 and b[28]<7 and b[29]<7 and b[30]<7 and b[31]<7 and b[32]<7 and b[33]<7 and b[34]<7 and b[35]<7:

                                    if b[0]+b[1]+b[2]+b[3]+b[4]+b[5] == 21 and b[6]+b[7]+b[8]+b[9]+b[10]+b[11] == 21 and b[12]+b[13]+b[14]+b[15]+b[16]+b[17] == 21 and b[18]+b[19]+b[20]+b[21]+b[22]+b[23] == 21 and b[24]+b[25]+b[26]+b[27]+b[28]+b[29] == 21 and b[30]+b[31]+b[32]+b[33]+b[34]+b[35] == 21:
                                        if b[0]+b[6]+b[12]+b[18]+b[24]+b[30] == 21 and b[1]+b[7]+b[13]+b[19]+b[25]+b[31] == 21 and b[2]+b[8]+b[14]+b[20]+b[26]+b[32] == 21 and b[3]+b[9]+b[15]+b[21]+b[27]+b[33] == 21 and b[4]+b[10]+b[16]+b[22]+b[28]+b[34] == 21 and b[5]+b[11]+b[17]+b[23]+b[29]+b[35] == 21:
                                            return render(request,'success.html')
                                        else:
                                            messages.info(request,'Error occured')
                                    else:
                                        messages.info(request,'Error occured')
                                else:
                                    messages.info(request,'all number should be less than 7')
                            else:
                                messages.info(request,'Numbers should not be repeat')
                        else:
                            messages.info(request,'Numbers should not be repeat')
                    else:
                        messages.info(request,'Numbers should not be repeat')
                else:
                    messages.info(request,'Numbers should not be repeat')
            else:
                messages.info(request,'Numbers should not be repeat')
        else:
            messages.info(request,'Numbers should not be repeat')
       
    z=[1,2,3,4,5,6]
    return render(request,'sudo1.html',{'b':z})

def sudo(request):
    if request.method=="POST":
        a=int(request.POST["1"])
        b=int(request.POST["2"])
        c=int(request.POST["3"])
        d=int(2)
        e=int(request.POST["5"])
        f=int(request.POST["6"])
        g=int(request.POST["7"])
        h=int(request.POST["8"])
        i=int(3)
        print(a+b+c)
        print(d+e+f)
        print(g+h+i)
        if a!=b and a!=c and d!=e and d!=f and g!=h and g!=i and a!=d and a!=g and b!=e and b!=h and c!=f and c!=i:
            if a<4 and b<4 and c<4 and d<4 and e<4 and f<4 and g<4 and h<4 and i<4:
                if a+b+c == 6 and d+e+f == 6 and g+h+i == 6:
                    if a+d+g == 6 and b+e+h == 6 and c+f+i == 6:
                        return render(request,'success.html')
                    else:
                        messages.info(request,'Error occured')
                else:
                        messages.info(request,'Error occured')
            else:
                messages.info(request,'all number should be less than 4')
        else:
            messages.info(request,'Numbers should not be repeat')
       
    z=[1,2,3]
    return render(request,'sudo.html',{'b':z})