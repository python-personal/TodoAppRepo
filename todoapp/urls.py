from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Listview),
    path('update/<int:id>/',views.updateView,name='update'),
    path('delete/<int:id>/',views.deleteView,name='delete'),
]
