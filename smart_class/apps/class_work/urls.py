from django.urls import path

from apps.class_work import views

app_name = "class_work"
urlpatterns = [
    path("", views.WorkListView.as_view(), name="list"),
    path("work/create/", views.WorkCreateView.as_view(), name="work_create"),
    path("work/<int:pk>/update/", views.WorkUpdateView.as_view(), name="work_update"),
    path("work/<int:pk>/delete/", views.WorkDeleteView.as_view(), name="work_delete"),
    path("computer/create/", views.ComputerCreateView.as_view(), name="computer_create"),
    path("computer/<int:pk>/update/", views.ComputerUpdateView.as_view(), name="computer_update"),
    path("computer/<int:pk>/delete/", views.ComputerDeleteView.as_view(), name="computer_delete"),
    path('computer/control/<int:pk>/', views.ComputerControlView.as_view(), name='computer_control'),
]
