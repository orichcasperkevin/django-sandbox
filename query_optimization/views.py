from django.http import HttpResponse
from .models import Product,Attribute,ProductAtrribute
from django.db import connection

def test_view(request):
    products = Product.objects.all()
    no_of_products = len(products)

    queries = connection.queries
    for query in queries:
        print(query['sql'])        

    return HttpResponse(no_of_products)


# def test_view(request):
#     no_of_products = Product.objects.count()

#     queries = connection.queries
#     for query in queries:
#         print(query['sql'])        

#     return HttpResponse(no_of_products)

# def test_laziness(request):

#     silver_stuff = ProductAtrribute.objects.filter(attribute=3)
#     silver_laptop = silver_stuff.filter(product=3)

#     print(silver_laptop)

#     queries = connection.queries
#     for query in queries:
#         print(query['sql']) 
#         print("\n")

#     return HttpResponse(silver_laptop)

def test_view(request):
    products = Product.objects.all().only('description')

    print(products)
    queries = connection.queries
    for query in queries:
        print(query['sql'])        
   
    return HttpResponse(products)