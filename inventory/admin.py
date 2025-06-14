from django.contrib import admin
from .models import Drug, Stock

class DrugStockInlineAdmin(admin.StackedInline):
    model = Stock
    extra = 0
    fields = ["batch_number", "quantity", "expiry_date", "added_on_date"]
    readonly_fields = ["added_on_date"]

@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    inlines = [DrugStockInlineAdmin]

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ["drug", "batch_number", "quantity", "expiry_date", "is_expired"]
    search_fields = ["drug__name", "batch_number"]
