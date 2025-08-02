from django.urls import path
from . import views 

urlpatterns = [
    path('',views.job_list,name= 'job_list'),
    path('add/',views.job_add,name='job_add'),
    path('edit/<int:pk>',views.job_edit,name='job_edit'),
    path('delete/<int:pk>/',views.job_delete,name='job_delete'),

]