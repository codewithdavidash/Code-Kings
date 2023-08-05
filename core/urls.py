from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from .views import *
from .forms import LoginForm, ChangePassword

urlpatterns = [
    path('questions/', ask_questions, name='questions'),
    path('search/', search, name='search'),
    path('account/', account, name='account'),
    path('add/', add, name='add'),
    path('', videos, name='videos'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='core/changepassword.html',
         success_url=reverse_lazy('changepassworddone'), form_class=ChangePassword), name='changepassword'),
    path('changepassworddone/', auth_views.PasswordChangeDoneView.as_view(
        template_name='core/changepassworddone.html'), name='changepassworddone'),
    path('detail/<int:pk>', detail, name='detail'),
    path('detail_twdcss/<int:pk>', detail_twdcss, name='detail_twdcss'),
    path('detail_py/<int:pk>', detail_python, name='detail_py'),
    path('detail_dj/<int:pk>', detail_dj, name='detail_dj'),
    path('delete-acct/<int:id>', delete_account, name='delete-acct'),
    # CRUD urls
    # HTML URLS
    path('create-html/', create_html, name='create-html'),
    path('update-html/<int:id>/', update_html, name='update-html'),
    path('delete-html/<int:id>/', delete_html, name='delete-html'),
    # Tailwindcss URLS
    path('create-twdcss/', create_twdcss, name='create-twdcss'),
    path('update-twdcss/<int:id>/', update_twdcss, name='update-twdcss'),
    path('delete-twdcss/<int:id>/', delete_twdcss, name='delete-twdcss'),
    # Python URLS
    path('create-py/', create_py, name='create-py'),
    path('update-py/<int:id>/', update_py, name='update-py'),
    path('delete-py/<int:id>/', delete_py, name='delete-py'),
    # Django URLS
    path('create-dj/', create_dj, name='create-dj'),
    path('update-dj/<int:id>/', update_dj, name='update-dj'),
    path('delete-dj/<int:id>/', delete_dj, name='delete-dj'),
]
