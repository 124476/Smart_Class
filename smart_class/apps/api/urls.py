from django.urls import path

from apps.api import views

app_name = "api"

urlpatterns = [
    path('works/', views.WorkListView.as_view(), name='work_list'),
    path('works/<int:pk>/', views.WorkDetailView.as_view(), name='work_detail'),
    path('computers/', views.ComputerListView.as_view(), name='computer_list'),
    path('computers/<int:pk>/', views.ComputerDetailView.as_view(), name='computer_detail'),
]
