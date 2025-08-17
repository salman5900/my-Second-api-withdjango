from  django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewset with it. 
# This will automatically create the URL patterns for us.
# The router will generate the URLs for the EmployeeView.
# no need for the / and the as_view() method as the router handles that.
# The basename is used to create the URL names for the viewset.
router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('students/', views.student_view, name='student_view'),
    path('students/<int:student_id>/', views.student_detail_view, name='student_detail'),

    # path('employees/', views.EmployeeView.as_view(), name='employee_view'),
    # path('employees/<int:emp_id>/', views.EmployeeDetailView.as_view(), name='employee_detail_view')

    # Include the router's URLs
    # This will automatically create the URLs for the EmployeeView.
    path('', include(router.urls)),

    path('blogs/', views.BlogView.as_view(), name='blog_view'),
    path('comments/', views.CommentView.as_view(), name='comment_view'),

    path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail_view'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment_detail_view'),

]