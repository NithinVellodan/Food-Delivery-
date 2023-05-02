import datetime
import json

from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from web.models import FoodOrder, ViewFood



@login_required(login_url="users/login/")
def food_delete(request,id):
    food_order = get_object_or_404(FoodOrder, id=id)
    food_order.delete()

    instances = ViewFood.objects.all()
    orders = FoodOrder.objects.filter(user=request.user).order_by("order_date")

    dates = [datetime.date.today() + timezone.timedelta(days=i) for i in range(7)]
    
    context = {
            "instances": instances,
            "dates":dates,
            "orders": orders
        }
            # return render(request, "index.html", context)
    return render(request, "users/home.html", context)


@login_required(login_url="users/login/")
def view_food(request):
    if request.method == "POST":
        food_item_id = request.POST.get("food_item_id")

        date_string = request.POST.get("date")
        date_obj = datetime.datetime.strptime(date_string, "%B %d, %Y")
        formatted_date = date_obj.strftime("%Y-%m-%d")
        
        food_item = get_object_or_404(ViewFood, pk=food_item_id)
    
        FoodOrder.objects.create(user=request.user, food_item=food_item,order_date=formatted_date)

        instances = ViewFood.objects.all()
        orders = FoodOrder.objects.filter(user=request.user,is_ordered=False).order_by("order_date")

        dates = [datetime.date.today() + timezone.timedelta(days=i) for i in range(7)]
    
        context = {
            "instances": instances,
            "dates":dates,
            "orders": orders
        }

        return render(request, 'users/home.html', context=context)
    else:  
        instances = ViewFood.objects.all()
        dates = [datetime.date.today() + timezone.timedelta(days=i) for i in range(7)]

        context = {
            "instances": instances,
            "dates":dates,
        }

        return render(request, 'users/home.html', context=context)


def success(request):
    # Get all the orders that belong to the current user
    user_orders = FoodOrder.objects.filter(user=request.user,is_ordered = False)

    # Delete each order in the queryset
    for order in user_orders:
        order.is_ordered =True
        order.save()
    return render(request, 'order.html')

