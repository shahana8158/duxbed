from django.contrib import admin

from .models import Category, SubCategory, Product,fill_your_cart,Career,CartItem,CustomerReview, Appointment


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(fill_your_cart)
admin.site.register(CartItem)
admin.site.register(CustomerReview)
admin.site.register(Appointment)



@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'resume']














