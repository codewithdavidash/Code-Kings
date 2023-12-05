from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from .models import *
from .forms import *

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request, f'Your Account Was Successfully Created {user_name}')
            return redirect('/login/')
        
    else:
        form = SignupForm()
    context = {
        'form': form
    }
    return render(request, 'core/signup.html', context)


@login_required
def index(request):
    html_css = HTML_CSS.objects.all()[0:16]
    js = JS.objects.all()[0:16]
    py = PY.objects.all()[0:16]
    dj = DJ.objects.all()[0:16]
    context = {
        'html_css': html_css,
        'js': js,
        'py': py,
        'dj': dj,
    }
    return render(request, 'core/index.html', context)


@login_required
def add(request):
    return render(request, 'core/add.html')

#   HTML AND CSS
#   READ
@login_required
def html_css_detail(request, pk):
    html_css = get_object_or_404(HTML_CSS, pk=pk)
    context = {
        'html_css': html_css
    }
    return render(request, 'core/html_css_detail.html', context)


#   CREATE
@login_required
def add_html_css(request):
    if request.method == 'POST':
        form = ADDHTMLCSSVIDS(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg = form.cleaned_data.get('title')
            messages.success(request, f'{msg} Was Sucessfully Posted!')
            return redirect('/')
    else:
        form = ADDHTMLCSSVIDS()
    context = {
        'form': form
    }
    return render(request, 'core/add_html_css.html', context)

#   Update
@login_required
def update_html_css(request, pk):
    html_css = HTML_CSS.objects.get(pk=pk)
    if request.method == 'POST':
        form = ADDHTMLCSSVIDS(request.POST, request.FILES, instance=html_css)
        if form.is_valid():
            form.save()
            msg = form.cleaned_data.get('title')
            messages.success(request, f'{msg} Was Sucessfully Reposted!')
            return redirect('/')
    else:
        form = ADDHTMLCSSVIDS(instance=html_css)
    context = {
        'form': form,
        'html_css': html_css,
    }            
    return render(request, 'core/update_html_css.html', context)

#   Delete
@login_required
def delete_html_css(request, pk):
    html_css = HTML_CSS.objects.get(pk=pk)
    if request.method == 'POST':
        html_css.delete()
        messages.success(request, 'Video Was Sucessfully Deleted!')
        return redirect('/')
    
    return render(request, 'core/delete_html_css.html', {
        'html_css': html_css
    })
    
#   JAVASCRIPT
#   READ
@login_required
def js_detail(request, pk):
    js = get_object_or_404(JS, pk=pk)
    context = {
        'js': js
    }
    return render(request, 'core/js_detail.html', context)


#   CREATE
@login_required
def add_js(request):
    if request.method == 'POST':
        form = JSVIDS(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg = form.cleaned_data.get('title')
            messages.success(request, f'{msg} Was Sucessfully Posted!')
            return redirect('/')
    else:
        form = JSVIDS()
    context = {
        'form': form
    }
    return render(request, 'core/add_js.html', context)

#   Update
@login_required
def update_js(request, pk):
    js = JS.objects.get(pk=pk)
    if request.method == 'POST':
        form = JSVIDS(request.POST, request.FILES, instance=js)
        if form.is_valid():
            form.save()
            msg = form.cleaned_data.get('title')
            messages.success(request, f'{msg} Was Sucessfully Reposted!')
            return redirect('/')
    else:
        form = JSVIDS(instance=js)
    context = {
        'form': form,
        'js': js,
    }            
    return render(request, 'core/update_js.html', context)

#   Delete
def delete_js(request, pk):
    js = JS.objects.get(pk=pk)
    if request.method == 'POST':
        js.delete()
        messages.success(request, 'Video Was Sucessfully Deleted!')
        return redirect('/')
    
    return render(request, 'core/delete_js.html', {
        'js': js
    })
    
#   PYTHON
#   READ
@login_required
def py_detail(request, pk):
    py = get_object_or_404(PY, pk=pk)
    context = {
        'py': py
    }
    return render(request, 'core/py_detail.html', context)


#   CREATE
@login_required
def add_py(request):
    if request.method == 'POST':
        form = PYVIDS(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg = form.cleaned_data.get('title')
            messages.success(request, f'{msg} Was Sucessfully Posted!')
            return redirect('/')
    else:
        form = PYVIDS()
    context = {
        'form': form
    }
    return render(request, 'core/add_py.html', context)

#   Update
@login_required
def update_py(request, pk):
    py = PY.objects.get(pk=pk)
    if request.method == 'POST':
        form = PYVIDS(request.POST, request.FILES, instance=py)
        if form.is_valid():
            form.save()
            msg = form.cleaned_data.get('title')
            messages.success(request, f'{msg} Was Sucessfully Reposted!')
            return redirect('/')
    else:
        form = PYVIDS(instance=py)
    context = {
        'form': form,
        'py': py,
    }            
    return render(request, 'core/update_py.html', context)

#   Delete
@login_required
def delete_py(request, pk):
    py = PY.objects.get(pk=pk)
    if request.method == 'POST':
        py.delete()
        messages.success(request, 'Video Was Sucessfully Deleted!')
        return redirect('/')
    
    return render(request, 'core/delete_py.html', {
        'py': py
    })
    
    
#   DJANGO
#   READ
@login_required
def dj_detail(request, pk):
    dj = get_object_or_404(DJ, pk=pk)
    context = {
        'dj': dj
    }
    return render(request, 'core/dj_detail.html', context)


#   CREATE
@login_required
def add_dj(request):
    if request.method == 'POST':
        form = DJVIDS(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg = form.cleaned_data.get('title')
            messages.success(request, f'{msg} Was Sucessfully Posted!')
            return redirect('/')
    else:
        form = DJVIDS()
    context = {
        'form': form
    }
    return render(request, 'core/add_dj.html', context)

#   Update
@login_required
def update_dj(request, pk):
    dj = DJ.objects.get(pk=pk)
    if request.method == 'POST':
        form = DJVIDS(request.POST, request.FILES, instance=dj)
        if form.is_valid():
            form.save()
            msg = form.cleaned_data.get('title')
            messages.success(request, f'{msg} Was Sucessfully Reposted!')
            return redirect('/')
    else:
        form = DJVIDS(instance=dj)
    context = {
        'form': form,
        'dj': dj,
    }            
    return render(request, 'core/update_dj.html', context)

#   Delete
@login_required
def delete_dj(request, pk):
    dj = DJ.objects.get(pk=pk)
    if request.method == 'POST':
        dj.delete()
        messages.success(request, 'Video Was Sucessfully Deleted!')
        return redirect('/')
    
    return render(request, 'core/delete_dj.html', {
        'dj': dj
    })
    
#   Search Functionalty
@login_required
def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_p = Q(Q(title__icontains=q))
        html_css = HTML_CSS.objects.filter(multiple_p)
        js = JS.objects.filter(multiple_p)
        py = PY.objects.filter(multiple_p)
        dj = DJ.objects.filter(multiple_p)
    else:
        html_css = HTML_CSS.objects.all()
        js = JS.objects.all()
        py = PY.objects.all()
        dj = DJ.objects.all()
    context = {
        'html_css': html_css,
        'js': js,
        'py': py,
        'dj': dj,
    }
    return render(request, 'core/search.html', context)


#   HTMLCOMMENTS!
@login_required
def comments(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.user
            var.save()
            return redirect('/comment/')
    else:
        form = CommentForm()
    data = Comment.objects.all()
    context = {
        'form': form,
        'data': data    
    }            
    return render(request, 'core/comment.html', context)

@login_required
def settings(request):
    usr = User.objects.all()
    context = {
        'usr': usr
    }
    return render(request, 'core/settings.html', context)


@login_required
def delete_usr(request, pk):
    usr = User.objects.get(pk=pk)
    if request.method == 'POST':
        usr.delete()
        messages.success(request, f'{usr.username} Was Sucessfully Deleted!')
        return redirect('settings')
    
    return render(request, 'core/delete_usr.html', {
        'usr': usr
    })

@login_required
def post_list(request):
    data = list(HTML_CSS.objects.values())
    return JsonResponse(data, safe=False)

def contact(request):
    return render(request, 'core/contact.html', {})