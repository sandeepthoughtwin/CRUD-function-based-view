from django.contrib import admin
from django.urls import path
from information import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.create_view, name = 'create'),
    path('list/',views.list_view, name = 'list'),
    path('update/<int:id>/',views.update_view, name = 'update'),
    path('delete/<id>', views.delete_view,name = 'delete' )
]
