from django.urls import path
from .views import *

urlpatterns = [
    path('edit/<int:pk>', UpdateTasks.as_view()),
    path('', ListTasks.as_view()),
    path('create', CreateTasks.as_view()),
    path('delete/<int:pk>', DeleteTasks.as_view())
]