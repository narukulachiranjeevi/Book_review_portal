from django.urls import path,reverse_lazy
from . import views
from django.contrib.auth.views import LogoutView,PasswordChangeView

urlpatterns = [
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name = 'logout'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('edit/',views.ProfileUpdateView.as_view(),name='profileUpdate'),
    path('change_password/', PasswordChangeView.as_view(template_name='account/change_password.html',success_url=reverse_lazy('password_change_done')), name='change_password'),
    path('password_change_done/', views.password_change_done, name='password_change_done'),
    path('<int:pk>/',views.profileView,name='profile'),
    path('<int:userId>/block',views.blockUser,name='blockUser'),
]