from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Stocks, Category
from .serializer import StockSerializer,CategorySerializer


@api_view(["GET"])
def all_stock(request):
    stockList = Stocks.objects.all()
    serializedData = StockSerializer(stockList, many=True)
    return Response(data=serializedData.data,
                    status=status.HTTP_200_OK)

@api_view(["GET"])
def all_category(request):
    catergoryList = Category.objects.all()
    serializedData = CategorySerializer(catergoryList, many=True)
    return Response(data=serializedData.data,
                    status=status.HTTP_200_OK)

@api_view(["GET"])
def get_stock_by_id(request, id):
    try:
        stock = Stocks.objects.get(pk=id)
        serializedData = StockSerializer(stock)
        return Response(data=serializedData.data,
                        status=status.HTTP_200_OK)
    except Stocks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def create_stock(request):
    serializedData = StockSerializer(data=request.data)
    print(request.data)
    if serializedData.is_valid():
        serializedData.save()
        return Response(data=serializedData.data,
                        status=status.HTTP_201_CREATED)

    return Response(data=serializedData.errors,
                    status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def create_category(request):
    serializedData = CategorySerializer(data=request.data)
    if serializedData.is_valid():
        serializedData.save()
        return Response(data=serializedData.data,
                        status=status.HTTP_201_CREATED)

    return Response(data=serializedData.errors,
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def edit_stock(request, id):
    try:
        stock = Stocks.objects.get(pk=id)
        serializedData = StockSerializer(stock, data=request.data)
        if serializedData.is_valid():
            serializedData.save()
            return Response(data=serializedData.data,
                            status=status.HTTP_200_OK)
        return Response(data=serializedData.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    except Stocks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def delete_stock(request, id):
    try:
        stock = Stocks.objects.get(pk=id)
        stock.delete()
        return Response(status=status.HTTP_200_OK)
    except Stocks.DoestNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)