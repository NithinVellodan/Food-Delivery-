# from django.urls import path
# from web import views

# app_name = "web"


# urlpatterns = [
#     path("", views.index, name="index")
# ]
from django.urls import path
from web import views

app_name = "web"


urlpatterns = [
    path('', views.view_food, name="view_food"),
    path('<int:id>/', views.food_delete, name="delete"),
    path('success/', views.success, name="success"),

]
