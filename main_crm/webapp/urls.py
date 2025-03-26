from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('activities/',views.get_activities,name="activities"),
    path('customers/',views.get_customers,name="customers"),
    path('employees/',views.get_employees,name="employees"),
    path('register/',views.register,name="register"),
    path('login/',views.Login,name="login"),
    path('logout/',views.log_out,name="logout"),
    path('create_employee/',views.createnew_employee,name="create_employee"),
    path('create_customer/',views.createnew_customer,name="create_customer"),
    path('create_activity/',views.createnew_activity,name="create_activity"),
    path('create_activitytype/',views.createnew_activitytype,name="create_activitytype"),
    path('activity/<int:activity_id>',views.get_activity,name="activity"),
    path('update_activity/<int:activity_id>',views.updatethe_activity,name="update_activity"),
    path('delete_activity/<int:activity_id>',views.delete_activity,name="delete_activity")
]