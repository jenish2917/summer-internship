from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()    
router.register('employees', views.EmployeeViewset, basename='employees')

urlpatterns = [
    path('students/', views.studentsView),
    path('Students/', views.studentsView),
    path('student/<int:pk>/', views.studentDetailView),
    path('Student/<int:pk>/', views.studentDetailView),   
    # path('employees/', views.Employees.as_view()),
    # path('employees/<str:pk>/', views.EmployeeDetail.as_view()),

    path('', include(router.urls)), 
    path('blogs/', views.BlogsView.as_view(), name='blogs'),
    path('comments/', views.CommentsView.as_view(), name='comments'),
]