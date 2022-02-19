from django.urls import path
from app_users.views import AnotherLoginView, AnotherLogoutView, another_register_view, top_up_your_balancet_view
from app_users.views import account_view

urlpatterns = [
    path('another_login/', AnotherLoginView.as_view(), name='another_login'),
    path('another_logout/', AnotherLogoutView.as_view(), name='another_logout'),
    path('register/', another_register_view, name='register'),
    path('<int:user_id>/', account_view, name='account'),
    path('<int:user_id>/top_up_your_balancet/', top_up_your_balancet_view, name='balancet'),
]
