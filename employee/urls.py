from django.urls import path
from .views import emp_create, emp_update, emp_delete, emp_list, emp_info

urlpatterns = [
    path("", emp_list, name="emp_list"),
    path("create/", emp_create, name="emp_create"),
    path("<slug:employ>/", emp_info, name="emp_info"),
    # path("<slug:slug>/update/", emp_update, name="emp_update"),
    # path("<slug:slug>/delete/", emp_delete, name="emp_delete"),
]
