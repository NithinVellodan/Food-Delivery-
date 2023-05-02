from django.contrib import admin
from web.models import FoodOrder,ViewFood

# Register your models here.


class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ["user", "food_item", "order_date"]


admin.site.register(FoodOrder,FoodOrderAdmin)


class ViewFoodAdmin(admin.ModelAdmin):
    list_display = ["id", "food_type", "title"]


admin.site.register(ViewFood,ViewFoodAdmin)