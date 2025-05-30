from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('stockview/',stock_view, name="stock view"),
    path('about/', about_view, name="about page"),
    path('webpage/', web_page, name="web page"),
    path('stockForm/', stock_form, name="create stock"),
    path('editStock/<int:id>/', edit_stock, name='edit stock'),
    path('deleteStock/<int:id>', delete_stock, name="delete stock")

] 