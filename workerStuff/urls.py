from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = (
    path('admin/', admin.site.urls),
    path('position/<str:string>', views.index, name='position'),
    path('signUp/', views.signUp_link, name='signUp'),
    path('contact/', views.contact, name='contact'),
    path('signIn/', views.signIn_link, name='signIn'),
    path('checkuser', views.checkusername),
    path('checkmail', views.checkmail),
    path('logout', views.logoutUser),
    path('askQuestion/', views.askQuestion, name='askQuestion'),
    path('makeRequest/', views.makeRequest, name='makeRequest'),
    path('password_change/', views. PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('', views.index, name='index'),
)
