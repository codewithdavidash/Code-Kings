from django.urls import path, reverse_lazy
from django.contrib.auth import views
from .views import *
from .forms import *

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('add/', add, name='add'),
    path('contact/', contact, name='contact'),
    path('settings/', settings, name='settings'),
    path('delete-user/<int:pk>/', delete_usr, name='delete_usr'),
    path('search/', search, name='search'),
    path('login/', views.LoginView.as_view(authentication_form=LoginForm, template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('html-and-css-videos-detail/<int:pk>/', html_css_detail, name='html_detail'),
    path('add-html-and-css/', add_html_css, name='add_html_css'),
    path('update-html-and-css/<int:pk>/', update_html_css, name='update_html_css'),
    path('delete-html-and-css/<int:pk>/', delete_html_css, name='delete_html_css'),
    path('js-videos-detail/<int:pk>/', js_detail, name='js_detail'),
    path('add-js/', add_js, name='add_js'),
    path('update-js/<int:pk>/', update_js, name='update_js'),
    path('delete-js/<int:pk>/', delete_js, name='delete_js'),
    path('py-videos-detail/<int:pk>/', py_detail, name='py_detail'),
    path('add-py/', add_py, name='add_py'),
    path('update-py/<int:pk>/', update_py, name='update_py'),
    path('delete-py/<int:pk>/', delete_py, name='delete_py'),
    path('dj-videos-detail/<int:pk>/', dj_detail, name='dj_detail'),
    path('add-dj/', add_dj, name='add_dj'),
    path('update-dj/<int:pk>/', update_dj, name='update_dj'),
    path('delete-dj/<int:pk>/', delete_dj, name='delete_dj'),
    path('comment/', comments, name='comments'),
    path('change-your-password/', views.PasswordChangeView.as_view(form_class=ChangePasswordForm, template_name='core/changepassword.html', success_url=reverse_lazy('changepassworddone')),  name='changepassword'),
    path('password_changed_successfully/', views.PasswordChangeDoneView.as_view(template_name='core/changepassworddone.html'),  name='changepassworddone'),
    path('post-json/', post_list, name='post-json')
]
