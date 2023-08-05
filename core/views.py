from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.


HTML_RESPONSE = """
    <h1 class='text-center mt-40 text-black'>
    Your Feedback was received succesfully
    <a href='/' class="underline text-blue-700">go back</a>
    </h1>
    <script src="https://cdn.tailwindcss.com"></script>
                """

@login_required
def ask_questions(request):
    if request.method == 'POST':
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        email = request.POST.get('email')
        print(sub, msg, email)
        send_mail(sub, msg, 'ashafokedavid@gmail.com', [email])
        return HttpResponse(HTML_RESPONSE)

    return render(request, 'core/ask_questions.html', {})

@login_required
def delete_account(request, id):
    acct = User.objects.get(id=id)
    account = User.objects.all()
    if request.method == 'POST':
        acct.delete()
        return redirect('/account/')
    return render(request, 'core/delete_acct.html', {
        'acct': acct,
        'account': account
    })

@login_required
def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(title__icontains=q) | Q(description__icontains=q))
        data1 = HTMLVideo.objects.filter(multiple_q)
        data2 = TailwindcssVideo.objects.filter(multiple_q)
        data3 = DjangoVideo.objects.filter(multiple_q)
        data4 = PythonVideo.objects.filter(multiple_q)
    else:
        data1 = HTMLVideo.objects.all()
        data2 = TailwindcssVideo.objects.all()
        data3 = DjangoVideo.objects.all()
        data4 = PythonVideo.objects.all()
    return render(request, 'core/search.html', {
        'data1': data1,
        'data2': data2,
        'data3': data3,
        'data4': data4,
    })

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request , 'Account was successfully Created for ' + user)
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {
        'form': form
    })

@login_required
def account(request):
    account = User.objects.all()
    return render(request, 'core/account.html', {
        'account': account
    })


@login_required
def videos(request):
    htmlvideos = HTMLVideo.objects.all()
    pyvideos = PythonVideo.objects.all()
    twcssvideos = TailwindcssVideo.objects.all()
    djvideos = DjangoVideo.objects.all()
    return render(request, 'core/videos.html', {
        'htmlvideo': htmlvideos,
        'pyvideo': pyvideos,
        'twcssvideo': twcssvideos,
        'djvideo': djvideos,
    })


@login_required
def add(request):
    return render(request, 'core/add.html', {})


##   CRUD - Create, Read, Update, Delete
@login_required
def create_html(request):
    if request.method == 'POST':
        form = CreateHTMLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateHTMLForm()
    return render(request, 'core/create_html.html', {
        'form': form,
    })

@login_required
def update_html(request, id):
    html = HTMLVideo.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateHTMLForm(request.POST or None, instance=html)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateHTMLForm()
    return render(request, 'core/update_html.html', {
        'form': form,
        'html': html
    })

@login_required
def delete_html(request, id):
    html = HTMLVideo.objects.get(id=id)
    form = UpdateHTMLForm(request.POST or None, instance=html)
    if request.method == 'POST':
        html.delete()
        return redirect('/')
    return render(request, 'core/delete_html.html', {
        'form': form,
        'html': html
    })

@login_required
def create_twdcss(request):
    if request.method == 'POST':
        form = CreateTWCSSForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateTWCSSForm()
    return render(request, 'core/create_twcss.html', {
        'form': form,
    })

@login_required
def update_twdcss(request, id):
    twcss = TailwindcssVideo.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateTWCSSForm(request.POST or None, instance=twcss)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateTWCSSForm()
    return render(request, 'core/update_twcss.html', {
        'form': form,
        'twcss': twcss
    })

@login_required
def delete_twdcss(request, id):
    twcss = TailwindcssVideo.objects.get(id=id)
    form = DeleteTWCSSForm(request.POST or None, instance=twcss)
    if request.method == 'POST':
        twcss.delete()
        return redirect('/')
    return render(request, 'core/delete_twcss.html', {
        'form': form,
        'twcss': twcss
    })

@login_required
def create_py(request):
    if request.method == 'POST':
        form = CreatePyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreatePyForm()
    return render(request, 'core/create_py.html', {
        'form': form,
    })

@login_required
def update_py(request, id):
    py = PythonVideo.objects.get(id=id)
    if request.method == 'POST':
        py = PythonVideo.objects.get(id=id)
        form = UpdatePyForm(request.POST or None, instance=py)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdatePyForm()
    return render(request, 'core/update_py.html', {
        'form': form,
        'py': py
    })

@login_required
def delete_py(request, id):
    py = PythonVideo.objects.get(id=id)
    form = DeleteTWCSSForm(request.POST or None, instance=py)
    if request.method == 'POST':
        py.delete()
        return redirect('/')
    return render(request, 'core/delete_py.html', {
        'form': form,
        'py': py
    })

@login_required
def create_dj(request):
    if request.method == 'POST':
        form = CreateDjForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateDjForm()
    return render(request, 'core/create_dj.html', {
        'form': form,
    })

@login_required
def update_dj(request, id):
    dj = DjangoVideo.objects.get(id=id)
    if request.method == 'POST':
        dj = DjangoVideo.objects.get(id=id)
        form = UpdateDjForm(request.POST or None, instance=dj)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateDjForm()
    return render(request, 'core/update_dj.html', {
        'form': form,
        'dj': dj
    })

@login_required
def delete_dj(request, id):
    dj = DjangoVideo.objects.get(id=id)
    form = DeleteDjForm(request.POST or None, instance=dj)
    if request.method == 'POST':
        dj.delete()
        return redirect('/')
    return render(request, 'core/delete_dj.html', {
        'form': form,
        'dj': dj
    })

@login_required
def detail(request, pk):
    html = get_object_or_404(HTMLVideo, pk=pk)
    return render(request, 'core/detail.html', {
        'html': html,
    })

@login_required
def detail_twdcss(request, pk):
    twdcss = get_object_or_404(TailwindcssVideo, pk=pk)
    return render(request, 'core/detail_twdcss.html', {
        'twdcss': twdcss,
    })

@login_required
def detail_python(request, pk):
    py = get_object_or_404(PythonVideo, pk=pk)
    return render(request, 'core/detail_py.html', {
        'py': py,
    })

@login_required
def detail_dj(request, pk):
    dj = get_object_or_404(DjangoVideo, pk=pk)
    return render(request, 'core/detail_dj.html', {
        'dj': dj,
    })