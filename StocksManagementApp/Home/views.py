from django.shortcuts import render, redirect
import requests as HttpReq
from django.http import HttpResponse
from .forms import StockForm



def dashboard(request):

    return render(request, 'dash.html')


def stock_view(request):
    requestObj = HttpReq.get("http://127.0.0.1:5656/stocks/allStock/")
    data = requestObj.json()
    return render(request, 'stockList.html', {"stockList": data})

def stock_form(request):
    categoryChoices = get_categories(request)
    if request.method == "POST":
        form =StockForm(request.POST)
        form.fields["categoryId"].choices = categoryChoices
        if form.is_valid():
            payload = form.cleaned_data
            res = HttpReq.post("http://127.0.0.1:5656/stocks/createStock/", json=payload)
            if res.status_code == 201:
                return redirect("stock view")
            return HttpResponse(f"API Error: {res.text}", status=res.status_code)
        return HttpResponse(f"Form Error: {form.errors}")
    else:
        form = StockForm()
        form.fields["categoryId"].choices = categoryChoices
    return render(request, "stockForm.html", {"form": form})

def edit_stock(request, id):
    categories = get_categories(request)
    if request.method == "POST":
        form = StockForm(request.POST)
        form.fields["categoryId"].choices = categories
        if form.is_valid():
            payload = form.cleaned_data
            res = HttpReq.put(f"http://127.0.0.1:5656/stocks/editStock/{id}", json=payload)
            if res.status_code == 200:
                return redirect("stock view")
            return HttpResponse(f"API Error: {res.text}", status=res.status_code)
        return HttpResponse(f"Form Error: {form.errors}")
    else:
        requestObj = HttpReq.get(f"http://127.0.0.1:5656/stocks/getStockById/{id}")
        jsonData = requestObj.json()
        jsonData["categoryId"] = jsonData["categoryId"].get("categoryName")
        form = StockForm(initial=jsonData)
        form.fields["categoryId"].choices = categories
        return render(request, "stockForm.html", {"form": form})

def delete_stock(request, id):
    if request.method == "POST":
        res = HttpReq.delete(f"http://127.0.0.1:5656/stocks/deleteStock/{id}")
        if res.status_code == 200:
            return redirect('stock view')
        return HttpResponse(f"API Error: {res.text}")

def about_view(request):
    return render(request, 'About.html')

def web_page(request):
    return render(request,'Webpage.html')

def get_categories(request):
    requestObj = HttpReq.get(f"http://127.0.0.1:5656/stocks/AllCategory/")
    if requestObj.status_code == 200:
        data = requestObj.json()
    else:
        data = []
    categoryChoices = []
    for item in data:
        categoryChoices.append((item["categoryId"], item["categoryName"]))
    return categoryChoices
