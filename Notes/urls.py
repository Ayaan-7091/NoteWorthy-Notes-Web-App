from django.contrib import admin
from django.urls import path,include
from Notes import views

urlpatterns = [
   
    path('', views.home,name="home"),
    # path('notes/', views.notes,name="notes"),
    path('notes/', views.NotesListView.as_view(),name="notes"),

    path('notes/<int:pk>/', views.details,name='details'),
    path('notes/new/',views.NotesCreateView.as_view(),name="create"),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(),name='update'),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(),name='delete'),
    path('login/', views.LoginInterfaceView.as_view(),name="login"),
    path('logout/', views.LogoutInterfaceView.as_view(),name="logout"),
    path('signup/', views.SignupView.as_view(),name="signup"),





    




]
