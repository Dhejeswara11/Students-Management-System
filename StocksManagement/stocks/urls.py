
from django.urls import path
from .views import *


urlpatterns = [
    path('allStock/', all_stock),
    path('createStock/', create_stock),
    path('getStockById/<int:id>', get_stock_by_id, name='getStockById'),
    path('editStock/<int:id>', edit_stock, name='edit stock'),
    path('deleteStock/<int:id>', delete_stock, name='delete stock'),
    path('AllCategory/', all_category),
]

