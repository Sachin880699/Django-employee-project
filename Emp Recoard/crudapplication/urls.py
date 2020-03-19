from django.urls import path
from crudapplication import views
app_name='crudapplication'

urlpatterns = [

    path('emp',views.emp, name ='emp'),
    path('', views.show, name ='show'),
    path('edit/<int:id>', views.edit, name ='edit'),
    path('update/<int:id>', views.update, name ='update'),
    path('delete/<int:id>', views.delete, name ='delete'),
]