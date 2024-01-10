from django.urls import path
from . import views

urlpatterns = [
        path('todos/', views.TodoApiList.as_view()),
        path('todos/<int:pk>', views.TodoDeleteUpdateGet.as_view()),
        path('todos/new/', views.TodoApiCreateList.as_view()),
]